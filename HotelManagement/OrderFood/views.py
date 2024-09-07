import traceback
from django.shortcuts import render
from Common.constants import BAD_REQUEST, MENU_ITEM_ADDED_SUCCESSFULLY, MENU_ITEM_DELETED_SUCCESSFULLY, ROOM_DETAILS_ADDED_SUCCESSFULLY, SERIALIZER_IS_NOT_VALID
from OrderFood.models import FoodMenu
from OrderFood.serializers import FoodMenuSerializer, OrderedFoodSerializer
from RoomBooking.models import Rooms
from Security.customer_authorization import CustomerJWTAuthentication
from exceptions.generic_response import GenericSuccessResponse
from RoomBooking.serializers import BookedRoomsSerializer, RoomBookingSerializer
from exceptions.generic import CustomBadRequest, GenericException
from Security.admin_authorization import AdminJWTAuthentication
from rest_framework.views import APIView


# Create your views here.
class FoodItems (APIView):

    authentication_classes = [AdminJWTAuthentication]

    @staticmethod
    def post(request):
        try:
            if "price" not in request.data or "description" not in request.data or "food_name" not in request.data:
                return CustomBadRequest(message = BAD_REQUEST)
            
            food_menu_serializer = FoodMenuSerializer(data = request.data)

            if food_menu_serializer.is_valid(raise_exception=True):
                room = food_menu_serializer.save()
                return GenericSuccessResponse(FoodMenuSerializer(room).data,message=MENU_ITEM_ADDED_SUCCESSFULLY)
            
            else:
                return GenericException(message=SERIALIZER_IS_NOT_VALID)
        
        except Exception as e:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
            return GenericException()
        
    @staticmethod
    def patch(request):
        try:
            if "food_id" not in request.data or "price" not in request.data or "description" not in request.data or "food_name" not in request.data:
                return CustomBadRequest(message = BAD_REQUEST)
            
            foodmenu = FoodMenu.objects.get(food_id = request.data['food_id'])
            food_menu_serializer = FoodMenuSerializer(data = request.data)

            if food_menu_serializer.is_valid(raise_exception=True):
                food = food_menu_serializer.update(foodmenu,request.data)
                return GenericSuccessResponse(FoodMenuSerializer(food).data,message=MENU_ITEM_ADDED_SUCCESSFULLY)
            
            else:
                return GenericException(message=SERIALIZER_IS_NOT_VALID)
        
        except Exception as e:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
            return GenericException()
        
    @staticmethod
    def delete(request):
        try:
            if "food_id" not in request.data:
                return CustomBadRequest(message = BAD_REQUEST)
            
            food_item = FoodMenu.objects.get(food_id = request.data['food_id']).delete() 
            
            return GenericSuccessResponse(food_item,message=MENU_ITEM_DELETED_SUCCESSFULLY)

        except Exception as e:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
            return GenericException()  
        

class FoodOrder(APIView):
    authentication_classes = [CustomerJWTAuthentication]
    
    @staticmethod
    def get(request):
        try:

            food_item = FoodMenu.objects.filter(is_available=True)

            serialized_foodmenu=[]
           
            for i in food_item:
                serialized_foodmenu.append(RoomBookingSerializer(i).data)
            
            return GenericSuccessResponse(serialized_foodmenu,message="foodmenu fetched")
        
        except Exception as e:      
            return GenericException()
        
    
    @staticmethod
    def post(request):
        try:
            customer = request.user

            request.data['customer'] = customer.customer_id
            
            if "food" not in request.data:
                return CustomBadRequest(message = BAD_REQUEST)  
            
            ordered_food_serializer = OrderedFoodSerializer(data = request.data)
            
            if ordered_food_serializer.is_valid(raise_exception=True):
                ordered_food = ordered_food_serializer.save()
                return GenericSuccessResponse(OrderedFoodSerializer(ordered_food).data, message="food ordered")
            
            else:
                return GenericException(message=SERIALIZER_IS_NOT_VALID)
            
        except Exception as e:      
            return GenericException()
        
                                                                                                                                                                                                                                                                                                                  