from django.urls import path
from .views import signup_view, login_view, user_info_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('me/', user_info_view, name='user-info'),
]
