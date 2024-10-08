# Generated by Django 5.0.2 on 2024-08-13 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Security', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffAuthTokens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.TextField(db_column='auth_access_token', null=True)),
                ('refresh_token', models.TextField(db_column='auth_refresh_token', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'hm_staff_auth_tokens',
            },
        ),
        migrations.DeleteModel(
            name='AdministratorAuthTokens',
        ),
        migrations.DeleteModel(
            name='RestaurantAuthTokens',
        ),
    ]
