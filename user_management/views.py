from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import *
from .serializers import *
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class DeliverViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = DeliverSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
