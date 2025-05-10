from rest_framework import serializers
from performance.models import Performance

class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ['id', 'artist', 'latitude', 'longitude']
