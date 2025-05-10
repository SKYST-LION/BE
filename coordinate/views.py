from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from performance.models import Performance
from .serializers import CoordinateSerializer

@api_view(['GET'])
def performance_coordinates(request):
    performances = Performance.objects.all()
    serializer = CoordinateSerializer(performances, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)