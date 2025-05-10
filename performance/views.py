from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Performance
from .serializers import PerformanceSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def get_performances(request):
    performances = Performance.objects.all()
    serializer = PerformanceSerializer(performances, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_performance_detail(request, pk):
    performance = get_object_or_404(Performance, pk=pk)
    serializer = PerformanceSerializer(performance)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_performance(request):
    serializer = PerformanceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)  # user는 access_token에서 추출됨
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

