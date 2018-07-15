from rest_framework import serializers
from .models import *
class FieldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Field
        fields = ['key','value','field_type']
class ProductSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True)
    class Meta:
        model = Product
        fields = ['name','fields','price']
    def create(self,data):
        fields = data.pop('fields')
        product = Product.objects.create(**data)
        for field in fields:
            newField = Field.objects.create(**field)
            product.fields.add(newField)
        return product
class PIRSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PIR
        fields = ['product','count']
class InventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventory
        fields = ['name','products']
