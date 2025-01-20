from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("booking_confirmation/", views.booking_confirmation, name="booking_confirmation"),
]