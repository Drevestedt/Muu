from django.shortcuts import render, redirect
from .forms import BookingForm

# Create your views here.
def base(request):
  return render(request, "base.html", {})

def home(request):
  if request == "POST":
    form = BookingForm(request.POST)

    if form.is_valid():
      name = form.cleaned_data["name"]
      email = form.cleaned_data["email"]
      phone = form.cleaned_data["phone"]
      date = form.cleaned_data["date"]
      time = form.cleaned_data["time"]
      party_size = form.cleaned_data["party_size"]

      form.save()
      return redirect("booking_confirmation")
  else:
    form = BookingForm()
  return render(request, "home.html", {"form":form})

def booking_confirmation(request):
  return render(request, "booking-conf.html", {})
