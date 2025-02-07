from django import forms
from .models import Bookings

class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = "__all__"
        widgets = {
            "date": forms.DateInput(attrs={"type":"date"}),
            "time": forms.TimeInput(attrs={"type":"time"}),
            "phone": forms.TextInput(attrs={"type":"tel"}),
        }
 