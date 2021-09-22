from django.db import models
from django.db.models.fields import CharField, FloatField
from category.models import Category


class Product(models.Model):
    name = CharField(max_length=25)
    price = FloatField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.name}'