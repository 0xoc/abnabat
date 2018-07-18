from rest_framework import serializers
from .models import PIR, Inventory


class PIRSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PIR
        fields = ['product','count']
class InventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventory
        fields = ['name','products']
