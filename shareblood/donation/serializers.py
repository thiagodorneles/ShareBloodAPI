"""
shareblood.donation.serializers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from rest_framework import serializers

from account.serializers import CustomAccountSerializer

from .models import Donation, DonationHistory, FavoriteBloodType


class FavoriteBloodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteBloodType
        fields = ('blood_type', )


class DonationHistorySerializer(serializers.ModelSerializer):
    donator = CustomAccountSerializer()

    class Meta:
        model = DonationHistory
        fields = ('donator', )


class DonationSerializer(serializers.ModelSerializer):
    donations = DonationHistorySerializer(many=True, read_only=True)
    donated = serializers.SerializerMethodField()
    favorite_blood_types =  FavoriteBloodTypeSerializer(many=True, read_only=True)

    def get_donated(self, obj):
        return obj.total_donated()

    class Meta:
        model = Donation
        fields = ('favored', 'needed', 'donated',
                  'start_date', 'end_date', 'description',
                  'owner', 'blood_bank', 'donations', 'favorite_blood_types', )
