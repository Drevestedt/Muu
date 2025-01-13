from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Booking

# Create your views here.
def book_table(request):
  if request.method == 'POST':
    form = Booking(request.POST)
    if form.is_valid():
      form.save()
      return render(request, 'booking/success.html')
  else:
    form = Booking()
  return render(request, 'booking/book_table.html', {'form': form})

#def booking(request):
  #return HttpResponse("Booking Page")