from rest_framework import viewsets, response
from rest_framework.decorators import action

from .serializers import *
from .services import CalculoFinalProducao


class FazendaViewSet(viewsets.ModelViewSet):
    serializer_class = FazendaSerializer
    queryset = Fazenda.objects.all()


class AlgodoeiraViewSet(viewsets.ModelViewSet):
    serializer_class = AlgodoeiraSerializer
    queryset = Algodoeira.objects.all()

    @action(methods=['get'], detail=False)
    def calcular(self, request, pk=None):
        calculo = CalculoFinalProducao()
        return response.Response(calculo.calcular(), status=200)


class MovimentoViewSet(viewsets.ModelViewSet):
    serializer_class = MovimentoSerializer
    queryset = Estoque.objects.all()


class EstoqueViewSet(viewsets.ModelViewSet):
    serializer_class = EstoqueSerializer
    queryset = Estoque.objects.all()