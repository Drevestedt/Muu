from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("<h1>Working Test</h1>")

def booking_confirmation(request):
  return HttpResponse("<h1>Booking Confirmation</h1>")
