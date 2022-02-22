from itertools import product
from multiprocessing import context
from django.shortcuts import render
from . models import Product
from . models import Category
def product_list(request):
    products=Product.objects.all().order_by('-date')
    categories=Category.objects.all().order_by('name')


    context={
        'products':products,
        'categories':categories
    }


    return render(request,'products.html',context=context)
