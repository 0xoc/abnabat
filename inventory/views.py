from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.

class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PIRSViewSet(viewsets.ModelViewSet):
    queryset = PIR.objects.all()
    serializer_class = PIRSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
