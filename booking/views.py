from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
from django.conf import settings
from .form import BookingForm

# Create your views here.
def landing_page(request):
    template_path = os.path.join(settings.BASE_DIR, 'index.html')
    with open(template_path, 'r') as file:
        return HttpResponse(file.read(), content_type='text/html')
    
def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_confirmation')
    else:
        form = BookingForm()
    return render(request, 'index.html', {'form': form})

def booking_confirmation(request):
    return render(request, "booking/booking_conf.html", {})