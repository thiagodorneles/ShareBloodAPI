from rest_framework import viewsets

from .models import Location
from .serializers import LocationSerializer


class LocationView(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    model = Location

    def get_queryset(self):
        return Location.objects.all()
