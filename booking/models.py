from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    num_of_guests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.date} - {self.time} - {self.num_of_guests}"
