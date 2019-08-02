from rest_framework.routers import DefaultRouter

from apps.building.views import BuildingViewSet
from apps.factory.views import FactoryViewSet
from apps.patent.views import PatentViewSet
from apps.product.views import ProductViewSet

router = DefaultRouter()
router.register(r'buildings', BuildingViewSet, basename='building')
router.register(r'factories', FactoryViewSet, base_name='factory')
router.register(r'patents', PatentViewSet, base_name='patent')
router.register(r'products', ProductViewSet, base_name='product')
