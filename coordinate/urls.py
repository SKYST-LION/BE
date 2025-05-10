from django.urls import path
from .views import performance_coordinates

urlpatterns = [
    path('map/', performance_coordinates),
]