import traceback
from django.shortcuts import render
from Common.constants import BAD_REQUEST, ITEM_ADDED_SUCCESSFULLY, ITEMS_FETCHED_SUCCESSFULLY, MENU_ITEM_ADDED_SUCCESSFULLY, MENU_ITEM_DELETED_SUCCESSFULLY, ROOM_DETAILS_ADDED_SUCCESSFULLY, ROOMINVENTORY_ADDED_SUCCESSFULLY, SERIALIZER_IS_NOT_VALID
from Inventory.tasks import get_roominventory_data
from Security.staff_authorization import StaffJWTAuthentication
from Inventory.models import Inventory
from Inventory.serializers import InventorySerializer, RoomInventorySerializer, RoomInventoryquantitySerializer
from OrderFood.models import FoodMenu
from OrderFood.serializers import FoodMenuSerializer
from RoomBooking.models import Rooms
from Security.customer_authorization import CustomerJWTAuthentication
from exceptions.generic_response import GenericSuccessResponse
from RoomBooking.serializers import BookedRoomsSerializer, RoomBookingSerializer
from exceptions.generic import CustomBadRequest, GenericException
from Security.admin_authorization import AdminJWTAuthentication
from rest_framework.views import APIView
from django.http import JsonResponse
from Inventory.tasks import get_roominventory_data

def get_roominventory_data_view(request):
    try:

        result = get_roominventory_data.delay()
        task_result = result.get(timeout=10)
        return JsonResponse(task_result)
    
    except Exception as e:

        return JsonResponse({
            "status": "error",
            "message": "An error occurred while fetching room inventory data."
        })

class InventoryManagement (APIView):

    authentication_classes = [AdminJWTAuthentication]

    @staticmethod
    def post(request):
        try:
            if  "price" not in request.data or "description" not in request.data or "item_name" not in request.data or "quantity" not in request.data:
                return CustomBadRequest(message = BAD_REQUEST)
            
            inventory_serializer = InventorySerializer(data = request.data)

            if inventory_serializer.is_valid(raise_exception=True):
                item = inventory_serializer.save()
                return GenericSuccessResponse(InventorySerializer(item).data,message=ITEM_ADDED_SUCCESSFULLY)
            
            else:
                return GenericException(message=SERIALIZER_IS_NOT_VALID)
        
        except Exception as e:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
            return GenericException()
        
    @staticmethod
    def patch(request):
        try:
            if "item_id" not in request.data or "price" not in request.data or "description" not in request.data or "item_name" not in request.data or "quantity" not in request.data:
                return CustomBadRequest(message = BAD_REQUEST)
            
            inventory = Inventory.objects.get(item_id = request.data['item_id'])
            inventory_serializer = InventorySerializer(data = request.data)

            if inventory_serializer.is_valid(raise_exception=True):
                item = inventory_serializer.update(inventory,request.data)
                return GenericSuccessResponse(InventorySerializer(item).data,message=MENU_ITEM_ADDED_SUCCESSFULLY)
          
            else:
                return GenericException(message=SERIALIZER_IS_NOT_VALID)
        
        except Exception as e:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
            return GenericException()
        
    @staticmethod
    def delete(request):
        try:
            if "item_id" not in request.data:
                return CustomBadRequest(message = BAD_REQUEST)
            
            item = Inventory.objects.get(item_id = request.data['item_id']).delete() 
            
            return GenericSuccessResponse(item,message=MENU_ITEM_DELETED_SUCCESSFULLY)

        except Exception as e:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
            return GenericException()  
        
class AddRoomInventory(APIView):
    authentication_classes = [AdminJWTAuthentication]
    
    @staticmethod
    def patch(request):
        try:
            if "is_roominventory" not in request.data or "item_id" not in request.data:
                return CustomBadRequest(message = BAD_REQUEST)
           
            inventory = Inventory.objects.get(item_id = request.data['item_id'])

            room_inventory_serializer = RoomInventorySerializer(data = request.data)

            if room_inventory_serializer.is_valid(raise_exception=True):
                item = room_inventory_serializer.update(inventory,request.data)
                return GenericSuccessResponse(RoomInventorySerializer(item).data,message=ROOMINVENTORY_ADDED_SUCCESSFULLY)
            
            else:
                return GenericException(message=SERIALIZER_IS_NOT_VALID)
        
        except Exception as e:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
            return GenericException()
        
    @staticmethod
    def get(request):
        try:
            items = Inventory.objects.all()
            inventory_serializer = InventorySerializer(items, many=True)

            return GenericSuccessResponse(inventory_serializer.data, message="ITEMS_FETCHED_SUCCESSFULLY")

        except Exception as e:
            return GenericException()

class RoomInventoryManagement(APIView):
    authentication_classes = [StaffJWTAuthentication]
    
    @staticmethod
    def patch(request):
        try:
            if "quantity" not in request.data or "item_id" not in request.data:
                return CustomBadRequest(message = BAD_REQUEST)
            
            inventory = Inventory.objects.get(item_id = request.data['item_id'])

            room_inventory_quantity_serializer = RoomInventoryquantitySerializer(data = request.data)

            if room_inventory_quantity_serializer.is_valid(raise_exception=True):
                item = room_inventory_quantity_serializer.update(inventory,request.data)
                return GenericSuccessResponse(RoomInventoryquantitySerializer(item).data,message=ROOMINVENTORY_ADDED_SUCCESSFULLY)
            
            else:
                return GenericException(message=SERIALIZER_IS_NOT_VALID)
        
        except Exception as e:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
             return GenericException()
        
    @staticmethod
    def get(request):
        try:

            items = Inventory.objects.filter(is_roominventory = True)
            inventory_serializer = InventorySerializer(items, many=True)

            return GenericSuccessResponse(inventory_serializer.data, message=ITEMS_FETCHED_SUCCESSFULLY)

        except Exception as e:
            return GenericException()



class DailyRoomInventoryManagement(APIView):
    @staticmethod
    def patch(request):
        try:
            room_inventory_ids = request.data.get('room_inventory', [])
            updated_items = []

            for item_id in room_inventory_ids:
                try:
                    inventory = Inventory.objects.get(item_id=item_id)
                    data = {'quantity': inventory.quantity + 1}
                    room_inventory_quantity_serializer = RoomInventoryquantitySerializer(inventory, data=data, partial=True)

                    if room_inventory_quantity_serializer.is_valid(raise_exception=True):
                        item = room_inventory_quantity_serializer.save()
                        updated_items.append(item)

                except Inventory.DoesNotExist:
                    GenericException(message="inventory does not exists")

            return GenericSuccessResponse([RoomInventoryquantitySerializer(item).data for item in updated_items], message="All items updated successfully")

        except Exception as e:
            return GenericException()


