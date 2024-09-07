from django.urls import path

from .views import  Logout, Registration, Login
#,  OTPVerification, ResetPassword, ForgotPassword, AllHolidays

app_name = "Staff"

urlpatterns = [
    path("registration/", Registration.as_view()),

    path("logout/", Logout.as_view()),

    path("login/", Login.as_view()),
]