from rest_framework import serializers, viewsets
from .serializers import CartSerializer
from .models import Cart


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
