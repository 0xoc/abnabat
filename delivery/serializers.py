from rest_framework import serializers
import user_management.serializers
from .models import *


class PackageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Package
        fields = ['client','products']

class DeliveryPackageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeliveryPackage
        fields = ['package','client']

class DeliverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deliver
        fields = ['deliver','deliveryPackages']

class DeliverySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Delivery
        fields = ['delivers']
