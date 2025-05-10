from rest_framework import serializers
from .models import Performance

class PerformanceSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(source='likes.count', read_only=True)
    created_by = serializers.StringRelatedField(read_only=True)
    is_liked = serializers.SerializerMethodField()
    
    class Meta:
        model = Performance
        fields = '__all__'
        
    def get_is_liked(self, obj):
        request = self.context.get('request')
        user = getattr(request, 'user', None)
        if not user or not user.is_authenticated:
            return False
        return obj.likes.filter(id=user.id).exists()
