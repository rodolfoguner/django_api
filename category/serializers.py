from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Category
from product.models import Product


class CategorySerializer(serializers.ModelSerializer):
    Product.products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = [
            'id', 
            'name',
            'products'
        ]
