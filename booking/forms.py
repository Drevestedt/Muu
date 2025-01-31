from django import forms

class BookingForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Phone", max_length=20)
    date = forms.DateField(label="Date")
    time = forms.TimeField(label="Time")
    party_size = forms.IntegerField(label="Party Size")
    