# Generated by Django 5.0.2 on 2024-08-16 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoomBooking', '0002_remove_rooms_date_from_remove_rooms_date_to_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
