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
    fields = ProducMetaSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'fields', 'price']

    def create(self, data):
        fields = data.pop('fields')
        product = Product.objects.create(**data)
        for field in fields:
            newField = Field.objects.create(**field)
            product.fields.add(newField)
        return product

    def update(self, instance, data):
        instance.name = data.get('name', instance.name)
        instance.price = data.get('price', instance.price)
        fields = data.pop('fields')
        i = 0
        for field in instance.fields.all():
            field.key = fields[i].get('key', field.key)
            field.value = fields[i].get('value', field.value)
            field.field_type = fields[i].get('field_type', field.field_type)
            field.save()
            i += 1
        instance.save()
        return instance
