from django.urls import path
from .views import get_performances, get_performance_detail, create_performance

urlpatterns = [
    path('', get_performances, name='performance_list'),  # /performance/
    path('<int:pk>/', get_performance_detail, name='performance_detail'),  # /performance/1/
    path('create/', create_performance, name='performance_create'),  # /performance/create/
]
