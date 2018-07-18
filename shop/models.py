from django.db import models
import os


class ProductMeta(models.Model):
    key = models.CharField(max_length = 255)
    value = models.CharField(max_length = 1200)
    field_type = models.CharField(max_length = 255)
    def __str__(self):
        return self.key + "->" + self.value

class ProductImageMeta(models.Model):
    img = models.ImageField(upload_to="%y/%m/%d/%s")

    def __str__(self):
        return os.path.basename(self.img.name)

class Product(models.Model):
    name = models.CharField(max_length = 255)
    fields = models.ManyToManyField(ProductMeta) #:)
    price = models.IntegerField()
    def __str__(self):
        return self.name

