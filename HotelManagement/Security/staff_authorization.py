import datetime
from django.shortcuts import render
from django.db.models import Q
from Staff.models import Staff

from Common.constants import SERIALIZER_IS_NOT_VALID, TOKEN_IS_EXPIRED
from Security.serializers import StaffAuthTokenSerializer
from exceptions.generic import CustomBadRequest, GenericException
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
import jwt


from django.conf import settings
from Security.models import StaffAuthTokens



def get_staff_authentication_token(staff):

    staff_refresh_token = jwt.encode(
        payload={
            "token_type": "refresh",
            "staff_id": staff.staff_id,
            "email": staff.email,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc) + settings.REFRESH_TOKEN_LIFETIME
        }, 
        key=settings.JWT_SECRET, 
        algorithm=settings.JWT_ALGORITHM
    )

    staff_access_token = jwt.encode(
        payload={
            "token_type": "access",
            "staff_id": staff.staff_id,
            "email": staff.email,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc) + settings.ACCESS_TOKEN_LIFETIME
        }, 
        key=settings.JWT_SECRET, 
        algorithm=settings.JWT_ALGORITHM
    )


    return {"staff_access_token":staff_access_token , "staff_refresh_token":staff_refresh_token}

def save_token(token):
    
    staff_auth_token_serializer = StaffAuthTokenSerializer(data={"access_token": token["staff_access_token"],"refresh_token":token["staff_refresh_token"]})

    if staff_auth_token_serializer.is_valid():
        staff_auth_token_serializer.save()
    
    else:
       return GenericException(message=SERIALIZER_IS_NOT_VALID)



class StaffJWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            header = request.headers.get("authorization")
            if not header:
                return CustomBadRequest(message="Authorization header missing")
            
            staff_token = header.split(" ")[1]

            if not StaffAuthTokens.objects.filter(Q(access_token=staff_token) | Q(refresh_token=staff_token)).exists():
                return CustomBadRequest(message=TOKEN_IS_EXPIRED)

        
            claims = jwt.decode(staff_token, key=settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
           
            staff = Staff.objects.get(staff_id=claims["staff_id"], email=claims["email"], is_deleted=False)

            return staff, claims
        
        except Staff.DoesNotExist:
            raise GenericException(message="Staff does not exist")
        
        except:
            GenericException()
        
