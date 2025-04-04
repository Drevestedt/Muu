from django.db import models

# Create your models here.
class Bookings(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone} - {self.date} - {self.time} - {self.party_size}"
    