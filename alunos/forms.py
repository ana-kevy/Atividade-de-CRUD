from django import forms
from django.forms import ModelForm
from .models import Aluno

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
        widgets = {
            # Informações pessoais
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'sexo': forms.Select(attrs={'class': 'form-control'}),  

            # Contato
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone_emergencia': forms.TextInput(attrs={'class': 'form-control'}),

            # Endereço
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.TextInput(attrs={'class': 'form-control'}),

            # Acadêmico
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),  # CORRIGIDO
            'serie_ano': forms.TextInput(attrs={'class': 'form-control'}),
            'turno': forms.Select(attrs={'class': 'form-control'}),  # choices
            'status': forms.Select(attrs={'class': 'form-control'}),  # choices
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
