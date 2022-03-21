from rest_framework import serializers
from client.serializers import ClientResponseSerializer
from product.serializers import ProductSerializer
from .models import Cart


class CartInputSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()
    owner = ClientResponseSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'
