from django.urls import path
from .views import get_performances, get_performance_detail, create_performance, update_performance, toggle_performance_like, top_liked_performances

urlpatterns = [
    path('', get_performances, name='performance_list'),  # /performance/
    path('<int:pk>/', get_performance_detail, name='performance_detail'),  # /performance/1/
    path('create/', create_performance, name='performance_create'),  # /performance/create/
    path('<int:pk>/edit/', update_performance, name='performance_edit'), # /performance/1/edit/
    path('<int:pk>/like/', toggle_performance_like, name='performance-like'),
    path('api/performances/top-liked/', name='top_liked_performances'),
]
