from itertools import product
from multiprocessing import context
from django.shortcuts import render
from . models import Product
def product_list(request):
    products=Product.objects.all().order_by('-date')

    context={
        'products':products
    }


    return render(request,'products.html',context=context)
