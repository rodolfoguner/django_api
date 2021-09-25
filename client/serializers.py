from cart.serializers import CartSerializer
from rest_framework import serializers
from .models import Client
from cart.serializers import CartSerializer


class ClientSerializer(serializers.ModelSerializer):
    carts = CartSerializer(many=True, read_only=True)
    class Meta:
        model = Client
        fields = [
            'id',
            'name',
            'cpf',
            'carts',
        ]
