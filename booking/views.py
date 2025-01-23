from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .form import BookingForm

# Create your views here.
class LandingPageView(TemplateView):
    template_name = "index.html"
    
def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_confirmation')
    else:
        form = BookingForm()
    return render(request, 'index.html', {'form': form})

def booking_confirmation(response):
    return render(response, "booking/booking_conf.html", {})