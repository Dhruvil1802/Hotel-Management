from OrderFood.models import FoodMenu, OrderedFood
from RoomBooking.models import BookedRooms

from rest_framework import serializers


class FoodMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodMenu
        fields = "__all__" 

class OrderedFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedFood
        fields = "__all__" 