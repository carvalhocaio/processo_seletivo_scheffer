from rest_framework import serializers
from .models import Fazenda, Algodoeira, Movimento, Estoque


class FazendaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Fazenda


class AlgodoeiraSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Algodoeira


class MovimentoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Movimento


class EstoqueSerializer(serializers.ModelSerializer):
    fardoes = serializers.IntegerField(read_only=True)
    rolinhos = serializers.IntegerField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Estoque