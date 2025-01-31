from django.shortcuts import render
from .forms import BookingForm

# Create your views here.
def base(response):
  return render(response, "base.html", {})

def home(response):
  if response == "POST":
    form = BookingForm(response.POST)
    
  form = BookingForm()
  return render(response, "home.html", {"form":form})
