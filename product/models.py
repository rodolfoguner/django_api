from django.db import models
from django.db.models.fields import CharField
from category.models import Category


class Product(models.Model):
    name = CharField(max_length=25)
    price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.name}'