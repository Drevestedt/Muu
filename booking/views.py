from django.shortcuts import render, redirect
from .forms import BookingForm

# Create your views here.
def base(request):
  return render(request, "base.html", {})

def home(request):
  if request.method == "POST":
    form = BookingForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("booking_confirmation")
    else:
      print("Form is invalid")
      print(form.errors)
  else:
    form = BookingForm()
    return render(request, "home.html", {"form":form})

def booking_confirmation(request):
  return render(request, "booking-conf.html", {})
