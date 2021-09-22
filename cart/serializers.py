from rest_framework import serializers
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True)
    class Meta:
        model = Cart
        fields = ['id','owner', 'total', 'products']
