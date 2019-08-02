from django.contrib import admin

from .models import Product, ProductOwners

admin.site.register(Product)
admin.site.register(ProductOwners)
