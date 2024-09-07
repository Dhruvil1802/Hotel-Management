from celery import shared_task
from datetime import date
from .models import BookedRooms

@shared_task
def check_and_finalize_bookings():
    today = date.today()
    print("celery done here")
    # Fetch all bookings that end today
    ending_bookings = BookedRooms.objects.filter(end_date=today)
    for booking in ending_bookings:
        # Perform necessary actions such as marking the booking as completed, sending a notification, etc.
        booking.status = 'completed'
        booking.save()
        # If an API call is needed, you can use the requests library or Django's reverse function.
        # For example:
        # requests.post('https://yourapi.com/endpoint', data={'booking_id': booking.id})
