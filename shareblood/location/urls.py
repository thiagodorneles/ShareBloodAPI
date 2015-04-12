from rest_framework.routers import DefaultRouter

from .views import LocationView


router = DefaultRouter()
router.register(r'', LocationView, 'location')

urlpatterns = router.urls
