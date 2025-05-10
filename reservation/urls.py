# reservation/urls.py

from django.urls import path
from .views import my_reservations

urlpatterns = [
    path('my/', my_reservations, name='my_reservations'),
]