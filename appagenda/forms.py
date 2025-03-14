from django import forms
from .models import Cidadao


class CidadaoForm(forms.ModelForm):
    class Meta:
        model = Cidadao
        fields = ['nome','cpf','email','data_nascimento','celular','cep','endereco','endereco_numero']
        labels = {
            'nome': 'Nome do Cidadão',
            'email': 'E-Mail',
            'cpf': 'C.P.F.',
            'data_nascimento':'Data de Nascimento',
            'endereco': 'Endereço',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'cpf':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),            
        }