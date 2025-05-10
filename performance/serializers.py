from rest_framework import serializers
from .models import Performance

class PerformanceSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Performance
        fields = [
            'id', 'artist', 'account', 'price', 'description', 'date', 'location',
            'latitude', 'longitude', 'cover_image',
            'created_by', 'created_at'
        ]
