"""
shareblood.location.serializers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('country', 'state', 'city', 'zipcode', 'street',
                  'neighborhood', 'latitude', 'longitude')
        model = Location
