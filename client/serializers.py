from rest_framework import serializers
from .models import Client
from .validators import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def validate(self, data):
        if not valid_name(data['name']):
            raise serializers.ValidationError({'name': 'Name should not content numbers'})
        if not valid_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf': 'CPF is not valid'})
        return data


class ClientResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'name')
