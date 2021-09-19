from client.serializers import ClientSerializer
from django.shortcuts import render
from rest_framework import viewsets
from .models import Client

#  Create a viewset thats returns the JSON
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
