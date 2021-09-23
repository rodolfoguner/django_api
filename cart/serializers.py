from rest_framework import serializers
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()
    class Meta:
        model = Cart
        exclude = []
