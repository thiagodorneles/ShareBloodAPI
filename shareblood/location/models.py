"""
shareblood.location.models
~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from django.db import models

from cities_light.models import City, Country, Region

class Location(models.Model):
    country = models.ForeignKey(Country, null=True, blank=True)
    state = models.ForeignKey(Region, null=True, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    zipcode = models.CharField(null=True, blank=True, max_length=255)
    street = models.CharField(null=True, blank=True, max_length=255)
    neighborhood = models.CharField(null=True, blank=True, max_length=255)
    latitude = models.BigIntegerField()
    longitude = models.BigIntegerField()
