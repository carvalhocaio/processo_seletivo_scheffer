from django.contrib import admin
from .models import Fazenda, Algodoeira


@admin.register(Fazenda)
class FazendaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'fardoes', 'rolinhos']


@admin.register(Algodoeira)
class AlgodoeiraAdmin(admin.ModelAdmin):
    list_display = ['nome', 'producao_diaria']
