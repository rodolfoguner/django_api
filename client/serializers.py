from django.db import models
from rest_framework import serializers
from .models import Client

#  Select the information that will be returned to the JSON
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'cpf']

