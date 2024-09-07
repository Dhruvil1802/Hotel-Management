from django.db import models

from Common.models import Audit
from Customer.models import Customers

# Create your models here.
class Rooms(Audit):
    class Meta:
        db_table = "hm_rooms"
    
    Room_id = models.BigAutoField(primary_key=True)
    price = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    is_cleaned = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    
class BookedRooms(Audit):
    class Meta:
        db_table = "hm_bookedrooms"
    
    BookedRoom_id = models.BigAutoField(primary_key=True)
    room = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    
    