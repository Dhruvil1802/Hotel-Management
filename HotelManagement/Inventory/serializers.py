from Inventory.models import Inventory


from rest_framework import serializers


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__" 

class RoomInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['is_roominventory']

class RoomInventoryquantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['quantity']