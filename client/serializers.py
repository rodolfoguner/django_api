from re import S
from rest_framework import serializers
from .models import Client
from cart.serializers import CartSerializer


class ClientSerializer(serializers.ModelSerializer):
    owners = CartSerializer(read_only=True)
    class Meta:
        model = Client
        exclude = []
