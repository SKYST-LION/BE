from django.shortcuts import render

# Create your views here.
# reservation/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Reservation
from .serializers import ReservationSerializer
from performance.models import Performance

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_reservation(request):
    performance_id = request.data.get('performance_id')
    quantity = request.data.get('quantity', 1)

    try:
        performance = Performance.objects.get(id=performance_id)
    except Performance.DoesNotExist:
        return Response({'error': '해당 공연이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)

    reservation = Reservation.objects.create(
        user=request.user,
        performance=performance,
        quantity=quantity,
        status='scheduled'
    )

    serializer = ReservationSerializer(reservation)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_reservations(request):
    user = request.user
    scheduled = Reservation.objects.filter(user=user, status='scheduled')
    completed = Reservation.objects.filter(user=user, status='completed')
    cancelled = Reservation.objects.filter(user=user, status='cancelled')

    def serialize(qs):
        return ReservationSerializer(qs, many=True).data

    return Response({
        "scheduled": serialize(scheduled),
        "completed": serialize(completed),
        "cancelled": serialize(cancelled),
    })