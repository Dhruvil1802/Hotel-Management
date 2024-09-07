from django.db import models

from Common.models import Audit


# Create your models here.
class Inventory(Audit):
    class Meta:
        db_table = "hm_inventory"
    
    item_id = models.BigAutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    is_roominventory = models.BooleanField(default=False)
    

