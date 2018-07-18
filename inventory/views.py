from rest_framework import viewsets

from .serializers import PIRSerializer, PIR, InventorySerializer, Inventory


class PIRSViewSet(viewsets.ModelViewSet):
    queryset = PIR.objects.all()
    serializer_class = PIRSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
