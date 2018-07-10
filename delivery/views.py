from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class DeliverViewSet(viewsets.ModelViewSet):
    queryset = Deliver.objects.all()
    serializer_class = DeliverSerializer

class DeliveryPackageViewSet(viewsets.ModelViewSet):
    queryset = DeliveryPackage.objects.all()
    serializer_class = DeliveryPackageSerializer
