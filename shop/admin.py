from django.contrib import admin

# Register your models here.
from shop.models import Product, ProductImageMeta, ProductMeta

admin.site.register(Product)
admin.site.register(ProductMeta)
admin.site.register(ProductImageMeta)
