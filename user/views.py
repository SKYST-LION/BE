from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


from .serializers import UserSignupSerializer, UserLoginSerialzer

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

        response = Response({
            "message" : "로그인 성공"
        }, status=status.HTTP_200_OK)

        response.set_cookie(
            key='access_token',
            value=access_token,
            httponly=True,
            samesite='Lax',
            secure=False
        )

        return response

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
