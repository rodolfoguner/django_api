from rest_framework import viewsets
from .serializers import CartInputSerializer
from .models import Cart


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartInputSerializer
    queryset = Cart.objects.all()
    