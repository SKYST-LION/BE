from rest_framework import serializers
from .models import Performance

class PerformanceSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(source='likes.count', read_only=True)
    created_by = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Performance
        fields = '__all__'
        
    def get_is_liked(self, obj):
        user = self.context.get('request').user
        return user.is_authenticated and obj.likes.filter(id=user.id).exists()
