# urls.py
from django.urls import path
from .views import create_artist, toggle_like_artist, my_liked_artists, artist_ranking

urlpatterns = [
    path('create/', create_artist, name='create-artist'),
    path('<int:artist_id>/like/', toggle_like_artist, name='like-artist'),
    path('likes/mine/', my_liked_artists, name='my-liked-artists'),
    path('ranking/', artist_ranking, name='artist-ranking'),
]