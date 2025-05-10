# artist/serializers.py

from rest_framework import serializers
from .models import Artist

class ArtistSerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField(read_only=True)  # 클라이언트에서 수정 불가

    class Meta:
        model = Artist
        fields = ['id', 'name', 'image', 'likes', 'created_by', 'created_at']
        read_only_fields = ['created_by', 'created_at']
