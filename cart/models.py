from enum import unique
from django.db import models
from client.models import Client
from product.models import Product
from django.db.models.signals import pre_save, post_save


class Cart(models.Model):
    owner = models.ForeignKey(Client,related_name='carts', on_delete=models.CASCADE)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    products = models.ManyToManyField(Product, related_name='carts')

    def __str__(self):
        return f'{self.id} {self.total}' 
