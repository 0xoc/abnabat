from django.db import models
from django.contrib.auth.models import User
import user_management.models
import inventory
# Create your models here.

class Package(models.Model):
    client = models.ForeignKey(user_management.models.Client,on_delete=models.CASCADE)
    products = models.ManyToManyField(inventory.models.Product)

class DeliveryPackage(models.Model):
    package = models.ForeignKey(Package,on_delete=models.CASCADE)
    client = models.ForeignKey(user_management.models.Client,on_delete=models.CASCADE)

class Deliver(models.Model):
    deliver = models.ForeignKey(user_management.models.Person,on_delete=models.CASCADE)
    deliveryPackages = models.ManyToManyField(DeliveryPackage)

class Delivery(models.Model):
    delivers = models.ManyToManyField(Deliver)
