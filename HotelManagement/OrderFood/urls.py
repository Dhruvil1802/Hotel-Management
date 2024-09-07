from django.urls import path
from .views import  FoodItems, FoodOrder 

app_name = "OrderFood"

urlpatterns = [
    path("fooditems/", FoodItems.as_view()),
    path("foodorder/", FoodOrder.as_view())

]