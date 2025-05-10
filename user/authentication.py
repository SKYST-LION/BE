from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
import logging

logger = logging.getLogger(__name__)

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get("access_token")
        logger.debug(f"Received cookies: {request.COOKIES}")
        logger.debug(f"Access token: {token}")

        if token is None:
            logger.debug("No access token found in cookies")
            return None

        try:
            validated_token = self.get_validated_token(token)
            user = self.get_user(validated_token)
            logger.debug(f"Successfully authenticated user: {user}")
            return user, validated_token
        except Exception as e:
            logger.error(f"Authentication failed: {str(e)}")
            raise AuthenticationFailed("유효하지 않은 토큰입니다.")
