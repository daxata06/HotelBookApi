from rest_framework import routers
from .views import HotelViewSet


router = routers.DefaultRouter()
router.register("hotels", HotelViewSet)
