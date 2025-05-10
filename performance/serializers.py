from rest_framework import serializers
from .models import Performance

class PerformanceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Performance
        fields = [
            'id', 'title', 'description', 'date', 'location',
            'cover_image', 'created_at'
        ]
