"""
shareblood.donation.models
~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from django.db import models

from shareblood import constants


class Donation(models.Model):
    favored = models.CharField(null=True, blank=True, max_length=255)
    needed = models.IntegerField(null=True, blank=True)
    donated = modelstart_date = models.DateField()s.IntegerField(null=True, blank=True)
    
    end_date = models.DateField()
    description = models.CharField(max_length=140)
    owner = models.ForeignKey('account.CustomAccount', related_name='owner_donation')
    blood_bank = models.ForeignKey('account.CustomAccount', related_name='blood_bank_donation')

class DonationHistory(models.Model):
    donator = models.ForeignKey('account.CustomAccount')
    date = models.DateField()
    donation = models.ForeignKey(Donation)

class FavoriteBloodTypes(models.Model):
    blood_type = models.CharField(max_length=2, choices=constants.BLOOD_TYPES)
    donation = models.ForeignKey(Donation)
