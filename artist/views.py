from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Artist
from .serializers import ArtistSerializer
from django.db.models import Count

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_artist(request):
    serializer = ArtistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_like_artist(request, artist_id):
    try:
        artist = Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        return Response({'error': '해당 아티스트가 존재하지 않아요'}, status=status.HTTP_404_NOT_FOUND)

    user = request.user

    if user in artist.likes.all():
        artist.likes.remove(user)
        return Response({'message': '좋아요 취소됨'}, status=status.HTTP_200_OK)
    else:
        artist.likes.add(user)
        return Response({'message': '좋아요 추가됨'}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_liked_artists(request):
    user = request.user
    liked_artists = Artist.objects.filter(likes=user)
    serializer = ArtistSerializer(liked_artists, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def artist_ranking(request):
    artists = Artist.objects.annotate(like_count=Count('likes')).order_by('-like_count', '-id')
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
