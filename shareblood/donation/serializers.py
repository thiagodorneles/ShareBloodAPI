"""
shareblood.donation.serializers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from rest_framework import serializers
from .models import Donation, DonationHistory

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ('favored', 'needed', 'donated', 'start_date', 'end_date', 'description', 'owner', 'blood_bank', 'donation__history' )

class DonationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationHistory
        fields = ('teste')