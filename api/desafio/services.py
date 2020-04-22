from datetime import datetime, timedelta

from .models import Estoque


class CalculoFinalProducao:

    def __init__(self, producao_fardao=22, producao_rolinho=5):
        self.producao_rolinho = producao_rolinho
        self.producao_fardao = producao_fardao

    def calcular(self):
        data = []

        for i in Estoque.objects.all():
            producao_diaria = i.algodoeira.producao_diaria
            fardos_produzir = (i.fardoes * self.producao_fardao) + (i.rolinhos * self.producao_rolinho)
            dias_produzindo = fardos_produzir / producao_diaria
            producao_ate = datetime.now().date() + timedelta(days=dias_produzindo)
            data.append(dict(producao_diaria=producao_diaria,
                             fardos_produzir=fardos_produzir,
                             dias_produzindo=dias_produzindo,
                             producao_ate=producao_ate))

        return data
