from re import search
from django.contrib import admin
from . models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price')
    search_fields=('name',)
