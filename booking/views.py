from django.shortcuts import render, redirect
from .form import BookingForm

# Create your views here.
def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_confirmation')
    else:
        form = BookingForm()
    return render(request, 'index.html', {'form': form})
