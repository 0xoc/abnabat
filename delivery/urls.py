from django.urls import path,include

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('packages',PackageViewSet)
router.register('deliveries',DeliveryViewSet)
router.register('delivers',DeliverViewSet)
router.register('delivery_packages',DeliveryPackageViewSet)
urlpatterns = [
    path('',include(router.urls)),

]
