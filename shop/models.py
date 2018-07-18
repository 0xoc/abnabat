from django.db import models
import os


class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    def __str__(self):
        return self.name

class ProductMeta(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="Origin")
    key = models.CharField(max_length = 255)
    value = models.CharField(max_length = 1200)
    field_type = models.CharField(max_length = 255)
    def __str__(self):
        return self.key + "->" + self.value

class ProductImageMeta(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="Origin")
    img = models.ImageField(upload_to="%y/%m/%d/%s")

    def __str__(self):
        return os.path.basename(self.img.name)

