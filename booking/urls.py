from django.urls import path
from . import views

urlpatterns = [
      path("", views.home, name="home"),
      path("booking_conf/", views.booking_confirmation, name="booking_confirmation"),
      path("edit_booking/<int:booking_id>/", views.edit_booking, name="edit_booking"),
      path("delete_booking/<int:booking_id>/", views.delete_booking, name="delete_booking"),
      path("delete_confirmation/", views.delete_confirmation, name="delete_confirmation"),
      path("find_booking/", views.find_booking, name="find_booking"),
]