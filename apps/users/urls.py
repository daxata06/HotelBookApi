from rest_framework import routers
from .views import CookieTokenObtainPairView, CookieTokenRefreshView
from django.urls import path

urlpatterns = [
    path('access/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
]