from django.urls import path
from . import views

urlpatterns = [
      path("", views.home, name="home"),
      path("booking_conf/", views.booking_confirmation, name="booking_conf"),
]