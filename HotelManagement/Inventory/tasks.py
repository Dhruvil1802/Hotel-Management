# from celery import shared_task
# from Inventory.models import Inventory
# from Inventory.serializers import InventorySerializer
# import traceback

# @shared_task
# def get_roominventory_data():
#     try:
#         items = Inventory.objects.filter(is_roominventory=True)
#         inventory_serializer = InventorySerializer(items, many=True)

#         return {
#             "status": "success",
#             "message": "ITEMS_FETCHED_SUCCESSFULLY",
#             "data": inventory_serializer.data
#         }

#     except Exception as e:

#         traceback.print_exc()
#         return {
#             "status": "error",
#             "message": "An error occurred while fetching room inventory data."
#         }
