from django.urls import path, include
from apps.building.views import BuildingViewSet
from apps.factory.views import FactoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'buildings', BuildingViewSet, basename='building')
router.register(r'factories', FactoryViewSet, base_name='factory')