from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Performance
from .serializers import PerformanceSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from collections import Counter


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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_performance_like(request, performance_id):
    performance = Performance.objects.get(id=performance_id)
    user = request.user

    if user in performance.likes.all():
        performance.likes.remove(user)
        return Response({'message': '좋아요 취소'}, status=status.HTTP_200_OK)
    else:
        performance.likes.add(user)
        return Response({'message': '좋아요 추가'}, status=status.HTTP_200_OK)

@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
def update_performance(request, pk):
    performance = get_object_or_404(Performance, pk=pk)

    # 권한 체크: 작성자만 수정 가능
    # if performance.created_by != request.user:
    #     return Response({"detail": "수정 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)

    serializer = PerformanceSerializer(performance, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def top_liked_performances(request):
    performances = Performance.objects.annotate(
        num_likes=Count('likes')
    ).order_by('-num_likes', 'id')[:3]
    serializer = PerformanceSerializer(performances, many=True, context={"request": request})
    return Response(serializer.data)

@api_view(['GET'])
def popular_songs(request):
    artist_name = request.GET.get('artist')
    limit = int(request.GET.get('limit', 10))
    order = request.GET.get('order', 'desc')

    # 1. 공연 필터링
    performances = Performance.objects.exclude(setlist__isnull=True).exclude(setlist='')

    if artist_name:
        performances = performances.filter(artist__icontains=artist_name)

    # 2. 곡 집계
    song_counter = Counter()
    for performance in performances:
        songs = [s.strip() for s in performance.setlist.split(',') if s.strip()]
        song_counter.update(songs)

    # 3. 정렬
    songs_sorted = (
        song_counter.most_common() if order == 'desc'
        else sorted(song_counter.items(), key=lambda x: x[1])
    )

    top_songs = songs_sorted[:limit]

    # 4. 응답 구성
    result = [{"title": title, "count": count} for title, count in top_songs]

    return Response(result, status=status.HTTP_200_OK)


