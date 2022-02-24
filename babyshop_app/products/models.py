from datetime import date
from distutils.command.upload import upload
from email.policy import default
from enum import unique
from pyexpat import model
from unicodedata import name
from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=50,null=True)
    slug=models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.name





class Product(models.Model):
    name=models.CharField(max_length=80)
    description=models.TextField()
    image=models.ImageField(upload_to="products/%Y/%m/%d/",default="products/broken-1.png")
    date=models.DateField(auto_now=True)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    category=models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)


    def __str__(self) -> str:
        return self.name