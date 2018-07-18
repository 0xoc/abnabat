from rest_framework import routers
from django.urls import path,include
from .views import PIRSViewSet, InventoryViewSet
router = routers.DefaultRouter()
router.register('pirs', PIRSViewSet)
router.register('invetories', InventoryViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
