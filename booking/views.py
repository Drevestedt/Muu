from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookings
from .forms import BookingForm

# Create your views here.
def base(request):
  return render(request, "base.html", {})

def home(request):
  if request.method == "POST":
    form = BookingForm(request.POST)
    if form.is_valid():
      booking = form.save()
      request.session["booking_id"] = booking.id
      return redirect("booking_confirmation")
    else:
      print("Form is invalid")
      print(form.errors)
      return render(request, "home.html", {"form":form})
  else:
    form = BookingForm()
  return render(request, "home.html", {"form":form})

def booking_confirmation(request):
  booking_id = request.session.get("booking_id")
  print("This is the booking id:", booking_id)
  if not booking_id:
        return redirect("home")
  
  booking = Bookings.objects.get(id=booking_id)
  return render(request, "booking_conf.html", {"booking":booking})

def edit_booking(request, booking_id):
  booking = get_object_or_404(Bookings, id=booking_id)
  if request.method == 'POST':
    form = BookingForm(request.POST, instance=booking)
    if form.is_valid():
      booking = form.save()
      request.session["booking_id"] = booking.id
      return redirect('booking_confirmation')
    else:
      print("Form is invalid")
      print(form.errors)
  else:
    form = BookingForm(instance=booking)
  return render(request, "edit_booking.html", {"form":form, "booking":booking})
  
def delete_booking(request, booking_id):
    booking = get_object_or_404(Bookings, id=booking_id)
    if request.method == "POST":
        booking.delete()
        return redirect("delete_confirmation")
    else:
       return render(request, "booking_conf.html", {"booking":booking})
  
def delete_confirmation(request):
    return render(request, "delete_conf.html", {})
