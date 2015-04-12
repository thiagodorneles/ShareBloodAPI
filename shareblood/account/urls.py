from rest_framework.routers import DefaultRouter

from .views import AccountView


router = DefaultRouter()
router.register(r'list', AccountView, 'list')

urlpatterns = router.urls
