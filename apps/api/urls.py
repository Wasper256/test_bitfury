from django.urls import path, include
from apps.building.views import BuildingViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api'

# urlpatterns = [
#     path('', include('apps.building.urls')),
# ]

router = DefaultRouter()
router.register(r'buildings', BuildingViewSet, basename='building')
# router.register(r'buildings.owners', BuildingOwnersViewSet, basename='owners')
urlpatterns = router.urls
