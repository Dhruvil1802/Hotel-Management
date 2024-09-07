from django.db import models

from Common.models import Audit



class Administrator(Audit):
    class Meta:
        db_table = 'hm_administrator'

    admin_id = models.BigAutoField(primary_key=True)

    admin_name = models.CharField(max_length=255)

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=255)

 
 
