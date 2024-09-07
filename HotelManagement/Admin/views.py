import re
import traceback
from django.shortcuts import render
from requests import Response
from Common.constants import BAD_REQUEST,  PASSWORD_LENGTH_SHOULD_BE_BETWEEN_8_TO_20, PASSWORD_MUST_HAVE_ONE_NUMBER, PASSWORD_MUST_HAVE_ONE_SMALLERCASE_LETTER, PASSWORD_MUST_HAVE_ONE_SPECIAL_CHARACTER, PASSWORD_MUST_HAVE_ONE_UPPERCASE_LETTER, USER_LOGGED_OUT_SUCCESSFULLY, USER_REGISTERED_SUCCESSFULLY

from Admin.serializers import RegistrationSerializer
from Admin.models import Administrator
from Security.admin_authorization import AdminJWTAuthentication
from Security.models import AdminAuthTokens
from Security.admin_authorization import AdminJWTAuthentication, get_admin_authentication_token, save_token

from exceptions.generic import BadRequest, CustomBadRequest, GenericException
from exceptions.generic_response import GenericSuccessResponse
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, ValidationError

from django.db.models import Q



class Registration(APIView):
    @staticmethod
    def post(request):
        try:
            
            if "password" not in request.data or "email" not in request.data or "admin_name" not in request.data:
                return CustomBadRequest(message=BAD_REQUEST)

            password = request.data["password"]
            special_characters = r"[\$#@!\*]"

          
            if len(password) < 8 or len(password) > 20:
                return CustomBadRequest(message=PASSWORD_LENGTH_SHOULD_BE_BETWEEN_8_TO_20)
            elif re.search('[0-9]', password) is None:
                return CustomBadRequest(message=PASSWORD_MUST_HAVE_ONE_NUMBER)
            elif re.search('[a-z]', password) is None:
                return CustomBadRequest(message=PASSWORD_MUST_HAVE_ONE_SMALLERCASE_LETTER)
            elif re.search('[A-Z]', password) is None:
                return CustomBadRequest(message=PASSWORD_MUST_HAVE_ONE_UPPERCASE_LETTER)
            elif re.search(special_characters, password) is None:
                return CustomBadRequest(message=PASSWORD_MUST_HAVE_ONE_SPECIAL_CHARACTER)


            registration_serializer = RegistrationSerializer(data=request.data)

            if registration_serializer.is_valid():

                admin = registration_serializer.save()
                tokens = get_admin_authentication_token(admin)
                save_token(tokens)

                return GenericSuccessResponse(tokens, message=USER_REGISTERED_SUCCESSFULLY)
            
            else:
                return CustomBadRequest(message="Invalid registration data")

        except Exception as e:
            return GenericException()
        
class Logout(APIView):
    authentication_classes = [AdminJWTAuthentication]

    @staticmethod
    def delete(request):
        try:
            header = request.headers.get("authorization")

            if not header:
                return CustomBadRequest(message="Authorization header missing")
            
            token = header.split(" ")[1]

            deletedtoken = AdminAuthTokens.objects.filter(Q(access_token=token) | Q(refresh_token=token)).delete()
           
            return GenericSuccessResponse(message=USER_LOGGED_OUT_SUCCESSFULLY)
        
        except Exception as e:
            return GenericException()
        
class Login(APIView):
    def post(self, request):
        try:
            email = request.data.get("email")
            password = request.data.get("password")

            if not email or not password:
                raise ValidationError(detail="Email and password are required.")
            
            customer = Administrator.objects.get(email=email, is_deleted=False)

            if not (password == customer.password):
                raise ValidationError(detail="Incorrect password.")
            
            authentication_tokens = get_admin_authentication_token(customer)
            save_token(authentication_tokens)
            return GenericSuccessResponse(authentication_tokens, message="USER_LOGGED_IN_SUCCESSFULLY")
        
        except Administrator.DoesNotExist:
            raise GenericException(message="Email not found.")
        
        except Exception as e:
            return GenericException(message= "An unexpected error occurred.")
