from rest_framework import serializers
from .models import Performance

class PerformanceSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Performance
        fields = [
            'id', 'title', 'description', 'date', 'location', 'created_by',
            'cover_image', 'created_at'
        ]
