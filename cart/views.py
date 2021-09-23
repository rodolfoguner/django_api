from rest_framework import serializers, viewsets
from .serializers import CartSerializer
from .models import Cart


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    