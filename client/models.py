from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    cpf = models.CharField(max_length=11, unique=True, blank=False, null=False)


    def __str__(self):
        return self.name
