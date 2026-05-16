from django.urls import path
from booking_app import views

urlpatterns = [
    path("rooms/", views.room_list, name="rooms-list"),
    path("booking/", views.book_room, name='book-room'),
]
