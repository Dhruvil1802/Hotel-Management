from django.db import models

class CustomerAuthTokens(models.Model):
    class Meta:
        db_table = 'hm_customer_auth_tokens'

    access_token = models.TextField(null=True, db_column="auth_access_token")
    refresh_token = models.TextField(null=True, db_column="auth_refresh_token")
    created_at = models.DateTimeField(auto_now_add=True)

class StaffAuthTokens(models.Model):
    class Meta:
        db_table = 'hm_staff_auth_tokens'

    access_token = models.TextField(null=True, db_column="auth_access_token")
    refresh_token = models.TextField(null=True, db_column="auth_refresh_token")
    created_at = models.DateTimeField(auto_now_add=True)

class AdminAuthTokens(models.Model):
    class Meta:
        db_table = 'hm_admin_auth_tokens'

    access_token = models.TextField(null=True, db_column="auth_access_token")
    refresh_token = models.TextField(null=True, db_column="auth_refresh_token")
    created_at = models.DateTimeField(auto_now_add=True)