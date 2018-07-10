from rest_framework import routers
from django.urls import path,include
from .views import *
router = routers.DefaultRouter()

router.register("users",UserViewSet)
router.register("persons",PersonViewSet)
router.register("delivers",DeliverViewSet)
router.register("clients",ClientViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
