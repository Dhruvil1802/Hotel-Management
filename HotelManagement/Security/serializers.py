from rest_framework import serializers

from .models import  AdminAuthTokens, StaffAuthTokens, CustomerAuthTokens


class CustomerAuthTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAuthTokens
        fields = ["access_token","refresh_token"]

class StaffAuthTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffAuthTokens
        fields = "__all__"

class AdminAuthTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminAuthTokens
        fields = "__all__"