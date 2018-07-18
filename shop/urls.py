from rest_framework import routers
from django.urls import path,include
from .views import ProductViewSet, ProductMetaViewSet, ProductImageMetaViewSet
router = routers.DefaultRouter()
router.register('fields', ProductMetaViewSet)
router.register('images', ProductImageMetaViewSet)
router.register('products', ProductViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
