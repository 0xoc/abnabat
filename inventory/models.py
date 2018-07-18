from django.db import models
import os
# Create your models here.
class Field(models.Model):
    key = models.CharField(max_length = 255)
    value = models.CharField(max_length = 1200)
    field_type = models.CharField(max_length = 255)
    def __str__(self):
        return self.key + "->" + self.value
class ImageField(models.Model):
    img = models.ImageField(upload_to="%y/%m/%d/%s")

    def __str__(self):
        return os.path.basename(self.img.name)
class Product(models.Model):
    name = models.CharField(max_length = 255)
    fields = models.ManyToManyField(Field) #:)
    price = models.IntegerField()
    def __str__(self):
        return self.name

class PIR(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="Origin")
    count = models.IntegerField()
class Inventory(models.Model):
    name = models.CharField(max_length = 255)
    products = models.ManyToManyField(PIR,related_name="Inventory");
    def __str__(self):
        return self.name
