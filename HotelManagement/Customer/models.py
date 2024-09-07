from django.db import models

from Common.models import Audit



class Customers(Audit):
    class Meta:
        db_table = 'hm_customers'

    customer_id = models.BigAutoField(primary_key=True)

    customer_name = models.CharField(max_length=255)

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=255)

 
 
