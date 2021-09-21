from django.db import models
from django.db.models.fields import FloatField
from client.models import Client
from product.models import Product


class Cart(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    total = FloatField()
    product = models.ManyToManyField(Product)
