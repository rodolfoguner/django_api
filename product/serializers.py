from rest_framework import serializers
from .models import Product
from category.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    #category = serializers.StringRelatedField(many=True)
    class Meta:
        model = Product
        fields = [
            'id', 
            'name', 
            'price',
            'category'
        ]
