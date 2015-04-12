"""
shareblood.donation.models
~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from django.db import models

from shareblood import constants

from simple_history.models import HistoricalRecords


class Donation(models.Model):
    favored = models.CharField(null=True, blank=True, max_length=255)
    needed = models.IntegerField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=140)
    owner = models.ForeignKey('account.CustomAccount', related_name='owner_donation')
    blood_bank = models.ForeignKey('account.CustomAccount', related_name='blood_bank_donation')
    history = HistoricalRecords()

    def total_donated(self):
        return self.donations.count()


class DonationHistory(models.Model):
    donator = models.ForeignKey('account.CustomAccount')
    donation = models.ForeignKey(Donation, related_name='donations')
    history = HistoricalRecords()

    class Meta:
        unique_together = ('donator', 'donation')


class FavoriteBloodType(models.Model):
    blood_type = models.CharField(max_length=2, choices=constants.BLOOD_TYPES)
    donation = models.ForeignKey(Donation)

    class Meta:
        unique_together = ('blood_type', 'donation')
