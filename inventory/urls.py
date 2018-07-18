from rest_framework import routers
from django.urls import path,include
from .views import *
router = routers.DefaultRouter()
router.register('fields',FieldViewSet)
router.register('image_fields',ImageFieldViewSet)
router.register('products',ProductViewSet)
router.register('pirs',PIRSViewSet)
router.register('invetories',InventoryViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
