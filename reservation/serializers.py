# reservation/serializers.py

from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    performance_artist = serializers.CharField(source='performance.artist', read_only=True)
    performance_location = serializers.CharField(source='performance.location', read_only=True)
    performance_date = serializers.DateTimeField(source='performance.date', read_only=True)

    class Meta:
        model = Reservation
        fields = [
            'id',
            'user',
            'performance',
            'performance_artist',
            'performance_location',
            'performance_date',
            'quantity',
            'status',
            'reserved_at',
        ]
        read_only_fields = ['user', 'reserved_at']