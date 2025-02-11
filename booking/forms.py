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

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if self.instance.pk is None:
            if Bookings.objects.filter(email=email).exists():
                raise forms.ValidationError("A booking already exists for this email.")
        return email
    