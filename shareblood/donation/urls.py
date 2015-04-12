from rest_framework.routers import DefaultRouter

from .views import DonationView


router = DefaultRouter()
router.register(r'', DonationView, 'donation')

urlpatterns = router.urls
