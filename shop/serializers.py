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
    ImageFields = ProductImageMetaSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'price','CharFields','ImageFields']

    def create(self, data):
        char_fields = data.pop('CharFields')
        image_fields = data.pop('ImageFields')

        # create raw prodcut
        product = Product.objects.create(**data)

        # Create char fields
        for char_field in char_fields:
            new_char_field = ProductMeta.objects.create(**char_field,product=product)

        # create Image Fileds
        for img_field in image_fields:
            new_img_filed = ProductImageMeta.objects.create(**img_field,product=product)
        
        return product
