from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    location = models.TextField()

    def __str__(self):
        return f'Room #{self.number} - {self.capacity}'
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="room")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Room #{self.user.username} - {self.room}"
    
