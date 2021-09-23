from re import S
from rest_framework import serializers
from .models import Client
from cart.models import Cart


class ClientSerializer(serializers.ModelSerializer):
    Cart.carts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Client
        fields = [
            'id', 
            'name', 
            'cpf',
            'carts',
        ]

