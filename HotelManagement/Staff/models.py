from django.db import models

from Common.models import Audit

# Create your models here.
class Staff(Audit):
    class Meta:
        db_table = 'hm_staff'

    staff_id = models.BigAutoField(primary_key=True)

    staff_name = models.CharField(max_length=255)

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=255)



