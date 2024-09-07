from django.urls import path
from .views import   AddRoomInventory, DailyRoomInventoryManagement, InventoryManagement, RoomInventoryManagement, get_roominventory_data_view 

app_name = "Inventory"

urlpatterns = [
    path("inventorymanagement/", InventoryManagement.as_view()),
    path("addroominventory/", AddRoomInventory.as_view()),
    path("roominventorymanagement/", RoomInventoryManagement.as_view()),
    path("dailyroominventorymanagement/", DailyRoomInventoryManagement.as_view()),
    path('getroominventorydataview/',get_roominventory_data_view)

]