from django.db import models

# Create your models here.
class Booking(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  date = models.DateField()
  time = models.TimeField()
  guest = models.PositiveBigIntegerField()

  def __str__(self):
    return f"{self.name} - {self.date} at {self.time}"
  