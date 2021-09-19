from django.db import models
from django.db.models.fields import CharField


class Category(models.Model):
    name = CharField(max_length=15)


    def __str__(self):
        return self.name
