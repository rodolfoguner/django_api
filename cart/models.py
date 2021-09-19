from django.db import models
from django.db.models.fields import FloatField
from client.models import Client


class Cart(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    total = FloatField()

    def __str__(self):
        return self.total
