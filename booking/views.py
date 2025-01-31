from django.shortcuts import render
from .forms import BookingForm

# Create your views here.
def base(response):
  return render(response, "base.html", {})

def home(response):
  if response == "POST":
    form = BookingForm(response.POST)
    if form.is_valid():
      name = form.cleaned_data["name"]
      email = form.cleaned_data["email"]
      phone = form.cleaned_data["phone"]
      date = form.cleaned_data["date"]
      time = form.cleaned_data["time"]
      party_size = form.cleaned_data["party_size"]
  else:
    form = BookingForm()
  return render(response, "home.html", {"form":form})

def booking_confirmation(response):
  return render(response, "booking-conf.html", {})
