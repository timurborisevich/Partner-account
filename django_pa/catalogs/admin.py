from django.contrib import admin
from .models import Products, ProductsGroup

# Register your models here.
admin.site.register(Products)
admin.site.register(ProductsGroup)