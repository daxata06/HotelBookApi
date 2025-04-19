from rest_framework.viewsets import ModelViewSet
from .serializers import HotelSerializer
from .models import Hotel


class HotelViewSet(ModelViewSet):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()
