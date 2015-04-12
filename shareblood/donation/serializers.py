"""
shareblood.donation.serializers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from rest_framework import serializers

from account.serializers import CustomAccountSerializer

from .models import Donation, DonationHistory


class DonationHistorySerializer(serializers.ModelSerializer):
    donator = CustomAccountSerializer()

    class Meta:
        model = DonationHistory
        fields = ('donator', )


class DonationSerializer(serializers.ModelSerializer):
    donations = DonationHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Donation
        fields = ('favored', 'needed', 'donated', 'start_date', 'end_date',
                  'description', 'owner', 'blood_bank', 'donations')
