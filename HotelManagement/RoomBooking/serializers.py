from RoomBooking.models import BookedRooms, Rooms

from rest_framework import serializers


class RoomBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = "__all__" 

class BookedRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedRooms
        fields = "__all__" 