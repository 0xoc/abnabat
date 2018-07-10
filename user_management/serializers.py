from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name']
class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['user']

class DeliverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deliver
        fields = ['user','status']
class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['user']
