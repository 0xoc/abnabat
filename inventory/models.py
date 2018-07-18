from django.db import models
import os

from shop.models import Product


class PIR(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="Origin")
    count = models.IntegerField()
class Inventory(models.Model):
    name = models.CharField(max_length = 255)
    products = models.ManyToManyField(PIR,related_name="Inventory");
    def __str__(self):
        return self.name
