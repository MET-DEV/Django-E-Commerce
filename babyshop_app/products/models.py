from datetime import date
from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models


class Product(models.Model):
    name=models.CharField(max_length=80)
    describtion=models.TextField()
    image=models.ImageField(upload_to="products/%Y/%m/%d/",default="products/broken-1.png")
    date=models.DateField(auto_now=True)
    price=models.DecimalField(max_digits=6,decimal_places=2)


    def __str__(self) -> str:
        return self.name