from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSignupSerializer, UserLoginSerialzer, UserSimpleSerializer

@api_view(['POST'])
def signup_view(request):
    serializer = UserSignupSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "회원가입이 완료되었습니다."}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors)
    

@api_view(['POST'])
def login_view(request):
    serializer = UserLoginSerialzer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        user_data = UserSimpleSerializer(user).data  # :흰색_확인_표시: 유저 정보 직렬화
        response = Response({
            "message": "로그인 성공",
            "user": user_data   # :흰색_확인_표시: 여기에 유저 정보 포함!
        }, status=status.HTTP_200_OK)
        response.set_cookie(
            key='access_token',
            value=access_token,
            httponly=True,
            samesite='Lax',
            secure=False  # 배포 시에는 True
        )
        return response
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info_view(request):
    user = request.user  # JWT 토큰에서 인증된 사용자

    return Response({
        "id": user.id,
        "email": user.email,
        "nickname": user.nickname,
    }, status=status.HTTP_200_OK)
