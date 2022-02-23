from datetime import date
from itertools import product
from multiprocessing import context
from unicodedata import category
from django.shortcuts import get_object_or_404, render
from . models import Product
from . models import Category
def product_list(request,category_slug=None):
    products=Product.objects.all().order_by('-date')
    categories=Category.objects.all().order_by('name')
    if category_slug != None:
        category_page=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.filter(category=category_page)

    context={
        'products':products,
        'categories':categories
    }


    return render(request,'products.html',context=context)
def product_detail(request,category_slug,product_id):
    product=Product.objects.get(category__slug=category_slug,id=product_id)
    products=Product.objects.all().order_by('-date')
    context={
        'product':product,
        'products':products[0:5],
    }
    return render(request,'product.html',context)