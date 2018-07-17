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
        fields = ['id','name','fields','price']
    def create(self,data):
        fields = data.pop('fields')
        product = Product.objects.create(**data)
        for field in fields:
            newField = Field.objects.create(**field)
            product.fields.add(newField)
        return product
    def update(self,instance,data):
        instance.name = data.get('name',instance.name)
        instance.price = data.get('price',instance.price)
        fields = data.pop('fields')
        i = 0
        for field in instance.fields.all():
            field.key = fields[i].get('key',field.key)
            field.value = fields[i].get('value',field.value)
            field.field_type = fields[i].get('field_type',field.field_type)
            field.save()
            i += 1
        instance.save()
        return instance


class PIRSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PIR
        fields = ['product','count']
class InventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventory
        fields = ['name','products']
