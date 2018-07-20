from rest_framework import serializers
from .models import ProductMeta, Product, ProductImageMeta


class ProductMetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductMeta
        fields = ['key', 'value', 'field_type']


class ProductImageMetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductImageMeta
        fields = ['id', 'img']


class ProductSerializer(serializers.ModelSerializer):
    CharFields = ProductMetaSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'CharFields', 'price']

    def create(self, data):
        char_fields = data.pop('CharFields')
        product = Product.objects.create(**data)
        for char_field in char_fields:
            new_char_field = ProductMeta.objects.create(**char_field,product=product)
        return product
