from django import forms
from .models import Cidadao, Atendimento, Agendamento


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
            'data_nascimento':forms.DateInput(attrs={'class':'form-control'}),
        }

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['cidadao','assunto','descricao','data_hora']
        labels = {
            'cidadao': 'Cidadão',
            'assunto': 'Assunto',
            'descricao': 'Descrição Detalhada',
            'data_hora': 'Data e Hora do Atendimento'
        }

class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ['descricao', 'decisoes','status']
        labels = {
            'descricao': 'Descrição do Atendimento',
            'decisoes': 'Decisões Tomadas',
            'status': 'Status',
        }