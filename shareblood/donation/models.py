"""
shareblood.donation.models
~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from django.db import models


class Donation(models.Model):
    favored = models.CharField(null=True, blank=True, max_length=255)
    needed = models.IntegerField(null=True, blank=True)
    donated = models.IntegerField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
