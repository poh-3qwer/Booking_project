from django.shortcuts import render, redirect
from .models import Room, Booking

def room_list(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }

    return render(request, template_name='booking_app/rooms_list.html', context=context)

def book_room(request):
    if request.method == "POST":
        room_number = request.POST.get('room-number')
        start_time = request.POST.get('start-time')
        end_time = request.POST.get('end-time')
        booking = Booking.objects.create(
            user=request.user,
            room=Room.objects.get(number=room_number),
            start_time=start_time,
            end_time=end_time 
        )
        return redirect('rooms-list')
    else:
        return render(request, 'booking_app/booking_form.html')
    
