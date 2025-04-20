from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .utils.jwt_cookies import set_jwt_cookies
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework import status
from settings.settings import SIMPLE_JWT
from rest_framework import generics
from .models import User
from .serializers import UserRegisterSerializer


class CookieTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get("access")
            refresh_token = response.data.get("refresh")

            if access_token and refresh_token:
                response = set_jwt_cookies(response, access_token, refresh_token)

                del response.data["access"]
                del response.data["refresh"]

        return response


class CookieTokenRefreshView(JWTAuthentication, TokenRefreshView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        raw_refresh_token = request.COOKIES.get(SIMPLE_JWT["REFRESH_COOKIE"]) or None
        raw_acces_token = request.COOKIES.get(SIMPLE_JWT["AUTH_COOKIE"]) or None
        data = {"access": raw_acces_token, "refresh": raw_refresh_token}

        serializer = self.get_serializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        response = Response(serializer.validated_data, status=status.HTTP_200_OK)

        access_token = response.data.get("access")
        refresh_token = response.data.get("refresh")

        if access_token and refresh_token:
            response = set_jwt_cookies(response, access_token, refresh_token)

            del response.data["access"]
            del response.data["refresh"]

        return response


class UserRegisterView(generics.GenericAPIView):
    permission_classes = ()
    authentication_classes = ()
    filter_backends = ()

    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        srz = self.get_serializer(data=request.data)
        srz.is_valid(raise_exception=True)
        srz.create()
        return Response(srz.data, status=status.HTTP_201_CREATED)
