# artist/serializers.py

from rest_framework import serializers
from .models import Artist

class ArtistSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ['id', 'name', 'likes_count']

    def get_likes_count(self, obj):
        return obj.likes.count()
