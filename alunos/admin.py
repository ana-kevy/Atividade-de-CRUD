from django.contrib import admin

from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 'matricula', 'email', 'curso', 'cidade', 'uf', 'turno', 'status'
    )
    list_display_links = ('nome',)
    search_fields = ('nome', 'matricula', 'cpf', 'email', 'cidade', 'curso')
    list_filter = ('curso', 'cidade', 'uf', 'turno', 'status')
    ordering = ('nome',)
    list_per_page = 25

    fields = (
        'nome', 'cpf', 'rg', 'data_nascimento', 'sexo',
        'email', 'telefone', 'telefone_emergencia',
        'cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'uf',
        'matricula', 'curso', 'serie_ano', 'turno', 'status',
        'observacoes',
    )


# Register your models here.

