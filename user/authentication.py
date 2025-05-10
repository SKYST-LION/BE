from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get("access_token")

        if token is None:
            return None

        validated_token = self.get_validated_token(token)

        try:
            return self.get_user(validated_token), validated_token
        except Exception:
            raise AuthenticationFailed("유효하지 않은 토큰입니다.")
