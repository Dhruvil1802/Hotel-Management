import traceback
from django.shortcuts import render
from Common.constants import BAD_REQUEST, ROOM_DETAILS_ADDED_SUCCESSFULLY, ROOM_DETAILS_DELETED_SUCCESSFULLY, SERIALIZER_IS_NOT_VALID
from RoomBooking.models import Rooms
from Security.customer_authorization import CustomerJWTAuthentication
from exceptions.generic_response import GenericSuccessResponse
from RoomBooking.serializers import BookedRoomsSerializer, RoomBookingSerializer
from exceptions.generic import CustomBadRequest, GenericException
from Security.admin_authorization import AdminJWTAuthentication
from rest_framework.views import APIView


# Create your views here.
class ManageRoom(APIView):

    authentication_classes = [AdminJWTAuthentication]

    @staticmethod
    def post(request):
        try:
            if "price" not in request.data or "description" not in request.data or "is_cleaned" not in request.data:
                return CustomBadRequest(message = BAD_REQUEST)
            
            room_booking_serializer = RoomBookingSerializer(data = request.data)

            if room_booking_serializer.is_valid(raise_exception=True):
                room = room_booking_serializer.save()
                return GenericSuccessResponse(RoomBookingSerializer(room).data,message=ROOM_DETAILS_ADDED_SUCCESSFULLY)
           
            else:
                return GenericException(message=SERIALIZER_IS_NOT_VALID)
        
        except Exception as e:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
            return GenericException()
        
    @staticmethod
    def patch(request):
        try:
            if "Room_id" not in request.data or "price" not in request.data or "description" not in request.data or "is_cleaned" not in request.data:
                return CustomBadRequest(message = BAD_REQUEST)
            
            room = Rooms.objects.get(Room_id=request.data["Room_id"])
            room_booking_serializer = RoomBookingSerializer(data=request.data)
            
            if room_booking_serializer.is_valid(raise_exception=True):
                room = room_booking_serializer.update(room,request.data)
                return GenericSuccessResponse(RoomBookingSerializer(room).data, message=ROOM_DETAILS_ADDED_SUCCESSFULLY)
            
            else:
                return GenericException(message=SERIALIZER_IS_NOT_VALID)
       
        except Exception as e:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
            return GenericException()
        
    @staticmethod
    def delete(request):
        try:
            if "Room_id" not in request.data :
                return CustomBadRequest(message = BAD_REQUEST)

            try:
                room = Rooms.objects.get(Room_id=request.data["Room_id"])
            except Rooms.DoesNotExist:
                return CustomBadRequest(message="Room not found")
            room.delete()

            return GenericSuccessResponse(message=ROOM_DETAILS_DELETED_SUCCESSFULLY)

        except Exception as e:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
            traceback.print_exc()
            return GenericException()
        
class BookRoom(APIView):
    authentication_classes = [CustomerJWTAuthentication]
   
    @staticmethod
    def get(request):
        try:
            rooms = Rooms.objects.filter(is_available=True)
            serialized_rooms=[]
            
            for i in rooms:
                serialized_rooms.append(RoomBookingSerializer(i).data)
            
            return GenericSuccessResponse(serialized_rooms,message="rooms fetched")
        
        except Exception as e:      
            return GenericException()
        
   
    @staticmethod
    def post(request):
        try:
            customer = request.user
            request.data['customer'] = customer.customer_id
            
            if "room" not in request.data or "date_to" not in request.data or "date_from" not in request.data:
                return CustomBadRequest(message = BAD_REQUEST)  
            
            booked_rooms_serializer = BookedRoomsSerializer(data = request.data)
            
            if booked_rooms_serializer.is_valid(raise_exception=True):
                booked_rooms = booked_rooms_serializer.save()
                return GenericSuccessResponse(BookedRoomsSerializer(booked_rooms).data, message="room booked")
            
            else:
                return GenericException(message=SERIALIZER_IS_NOT_VALID)
       
        except Exception as e:      
            return GenericException()
        
