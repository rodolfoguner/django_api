from django.db.models import manager
from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()
    class Meta:
        model = Cart
        fields = '__all__'
