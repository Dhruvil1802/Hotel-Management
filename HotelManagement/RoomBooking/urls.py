from django.urls import path
from .views import  BookRoom, ManageRoom

app_name = "RoomBooking"

urlpatterns = [
    path("manageroom/", ManageRoom.as_view()),
    path("bookroom/", BookRoom.as_view()),

]