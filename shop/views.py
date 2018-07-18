from rest_framework import viewsets

from shop.models import ProductMeta, ProductImageMeta, Product
from .serializers import ProductMetaSerializer, ProductImageMetaSerializer, ProductSerializer

class ProductMetaViewSet(viewsets.ModelViewSet):
    queryset = ProductMeta.objects.all()
    serializer_class = ProductMetaSerializer
class ProductImageMetaViewSet(viewsets.ModelViewSet):
    queryset = ProductImageMeta.objects.all()
    serializer_class = ProductImageMetaSerializer
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer