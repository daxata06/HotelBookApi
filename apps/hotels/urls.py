from rest_framework import routers
from .views import HotelViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'hotels', HotelViewSet, basename='hotel')

urlpatterns = [
    path('', include(router.urls)),
]