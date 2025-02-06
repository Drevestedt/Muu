from django.shortcuts import render, redirect
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
  else:
    form = BookingForm()
    return render(request, "home.html", {"form":form})

def booking_confirmation(request):
  booking_id = request.session.get("booking_id")
  if booking_id:
    booking = Bookings.objects.get(id=booking_id)
  return render(request, "booking-conf.html", {"booking":booking})
