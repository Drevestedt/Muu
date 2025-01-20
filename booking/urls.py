from django.urls import path
from . import views

urlpatterns = [
  path('book/', views.book_table, name='book_table'),
  path('booking-confirmation/', views.booking_confirmation, name='booking_confirmation'),  
]