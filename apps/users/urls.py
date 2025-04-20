from .views import (
    CookieTokenObtainPairView,
    CookieTokenRefreshView,
    UserRegisterView,
)
from django.urls import path

urlpatterns = [
    path("access/", CookieTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", CookieTokenRefreshView.as_view(), name="token_refresh"),
    path("register/user/", UserRegisterView.as_view(), name="register_user"),
]
