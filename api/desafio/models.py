from django.db import models


class Fazenda(models.Model):
    nome = models.CharField(max_length=100)
    fardoes = models.IntegerField()
    rolinhos = models.IntegerField()

    def __str__(self):
        return self.nome


class Algodoeira(models.Model):
    nome = models.CharField(max_length=100)
    producao_diaria = models.IntegerField()

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        super().save(*args, *kwargs)
        Estoque.objects.update_or_create(algodoeira=self)


class Movimento(models.Model):
    fazenda = models.ForeignKey('desafio.Fazenda', on_delete=models.CASCADE)
    algodoeira = models.ForeignKey('desafio.Algodoeira', on_delete=models.CASCADE)
    fardoes = models.IntegerField()
    rolinhos = models.IntegerField()

    def __str__(self):
        return f'{self.pk}'


class Estoque(models.Model):
    algodoeira = models.ForeignKey('desafio.Algodoeira', on_delete=models.CASCADE)

    @property
    def fardoes(self):
        return sum([i.fardoes for i in Movimento.objects.filter(algodoeira=self.algodoeira)]) or 0

    @property
    def rolinhos(self):
        return sum([i.rolinhos for i in Movimento.objects.filter(algodoeira=self.algodoeira)]) or 0