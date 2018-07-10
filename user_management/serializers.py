from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = User
        fields = ['name','last_name']
class PersonSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['user']

class DeliverSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Deliver
        fields = ['user','status']
class ClientSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['user']
