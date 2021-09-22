from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 
            'name', 
            'price',
        ]
