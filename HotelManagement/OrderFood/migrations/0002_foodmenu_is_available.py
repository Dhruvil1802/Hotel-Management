# Generated by Django 5.0.2 on 2024-08-20 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderFood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodmenu',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
