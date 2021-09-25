from django.db.models import manager
from product.serializers import ProductSerializer
from rest_framework import serializers
from .models import Cart
from product.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()
    products = ProductSerializer(many=True)
    class Meta:
        model = Cart
        fields = [
            'id',
            'total',
            'owner',
            'products',
        ]
