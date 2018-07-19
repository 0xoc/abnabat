from django.db import models
import os

from taxonomy.models import Term


class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    def __str__(self):
        return self.name

class ProductMeta(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="ProductOrigin")
    key = models.CharField(max_length = 255)
    value = models.CharField(max_length = 1200)
    field_type = models.CharField(max_length = 255)
    def __str__(self):
        return self.key + "->" + self.value

class ProductImageMeta(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="ImageOrigin")
    img = models.ImageField(upload_to="%y/%m/%d/%s")
    terms = models.ManyToManyField(Term, blank=True)
    def __str__(self):
        return os.path.basename(self.img.name)
