from django.db import models

from Common.models import Audit
from Customer.models import Customers

# Create your models here.
class FoodMenu(Audit):
    class Meta:
        db_table = "hm_foodmenu"
    
    food_id = models.BigAutoField(primary_key=True)
    food_name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    
class OrderedFood(Audit):
    class Meta:
        db_table = "hm_orderedfood"
    
    orderedfood_id = models.BigAutoField(primary_key=True)
    food = models.ForeignKey(FoodMenu, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)

    
    