import datetime
import traceback
from django.db.models import Q
from Customer.models import Customers

from Common.constants import SERIALIZER_IS_NOT_VALID, TOKEN_IS_EXPIRED
from Security.serializers import CustomerAuthTokenSerializer
from exceptions.generic import CustomBadRequest, GenericException
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
import jwt


from django.conf import settings
from Security.models import CustomerAuthTokens



def get_authentication_token(customer):

    customer_refresh_token = jwt.encode(
        payload={
            "token_type": "refresh",
            "customer_id": customer.customer_id,
            "email": customer.email,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc) + settings.REFRESH_TOKEN_LIFETIME
        }, 
        key=settings.JWT_SECRET, 
        algorithm=settings.JWT_ALGORITHM
    )
        
    customer_access_token = jwt.encode(
        payload={
            "token_type": "access",
            "customer_id": customer.customer_id,
            "email": customer.email,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc) + settings.ACCESS_TOKEN_LIFETIME
        }, 
        key=settings.JWT_SECRET, 
        algorithm=settings.JWT_ALGORITHM
    )


    return {"customer_access_token":customer_access_token , "customer_refresh_token":customer_refresh_token}

def save_token(token):
    
    customer_auth_token_serializer = CustomerAuthTokenSerializer(data={"access_token": token["customer_access_token"],"refresh_token":token["customer_refresh_token"]})

    if customer_auth_token_serializer.is_valid():
        customer_auth_token_serializer.save()
    
    else:
        return GenericException(message=SERIALIZER_IS_NOT_VALID)

        
class CustomerJWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            auth_header = request.headers.get("authorization")
            
            if not auth_header:
                raise GenericException(message="Authorization header missing")
            
            token_parts = auth_header.split()
            
            if len(token_parts) != 2 or token_parts[0].lower() != "bearer":
                raise GenericException(message="Invalid token header format")

            customer_token = token_parts[1]

            if not CustomerAuthTokens.objects.filter(Q(access_token=customer_token) | Q(refresh_token=customer_token)).exists():
                raise GenericException(message=TOKEN_IS_EXPIRED)

            claims = jwt.decode(customer_token, key=settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
            customer = Customers.objects.get(customer_id=claims["customer_id"], email=claims["email"], is_deleted=False)

            return customer, customer_token

        except Customers.DoesNotExist:
            raise GenericException(message="Customer does not exist")
        
        except Exception as e:
            raise GenericException(message="Authentication failed")
