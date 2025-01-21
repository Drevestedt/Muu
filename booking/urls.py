from django.urls import path
from . import views

urlpatterns = [
  path('book_table/', views.book_table, name='book_table'),
  path('booking_confirmation/', views.booking_confirmation, name='booking_confirmation'),
]