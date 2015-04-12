from rest_framework import permissions, viewsets

from rest_framework.permissions import AllowAny

from .models import Donation, DonationHistory
from .serializers import DonationSerializer, DonationHistorySerializer

class DonationView(viewsets.ModelViewSet):
    serializer_class = DonationSerializer
    model = Donation

    def get_queryset(self):
        return Donation.objects.all()

class DonationHistoryView(viewsets.ModelViewSet):
    serializer_class = DonationHistorySerializer
    model = DonationHistory

    def get_queryset(self):
        return DonationHistory.objects.all()
