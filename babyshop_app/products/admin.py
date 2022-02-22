from re import search
from django.contrib import admin
from . models import Category, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price')
    search_fields=('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
