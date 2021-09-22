from re import S
from rest_framework import serializers
from .models import Client
from cart.models import Cart


class ClientSerializer(serializers.ModelSerializer):
    Cart.carts = serializers.StringRelatedField(many=True)
    class Meta:
        model = Client
        fields = [
            'id', 
            'name', 
            'cpf',
            'carts'
        ]

