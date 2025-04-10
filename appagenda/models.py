from email.policy import default
from random import choices
from tokenize import blank_re
from django.db import models

# Create your models here.

class Cidadao(models.Model):
    nome = models.TextField(null=False)
    cpf = models.CharField(max_length=14, null=True)
    email = models.EmailField(unique=True)
    data_nascimento=models.DateField()
    celular = models.CharField(max_length=14, null=False)
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=200)
    endereco_numero=models.CharField(max_length=20)
    data_info = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome



class Agendamento(models.Model):
        STATUS_CHOICES = [
            ('A', 'Agendado'),
            ('C', 'Cancelado'),
            ('R', 'Realizado')
        ]

        cidadao = models.ForeignKey(Cidadao, on_delete=models.CASCADE, related_name='agendamentos')
        assunto = models.CharField(max_length=255)
        descricao = models.TextField()
        data_hora = models.DateTimeField()
        status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')

        def __str__(self):
            return f'Agendamento: {self.assunto} - {self.cidadao.nome} ({self.get_status_display()}) '

        def criar_atendimento(self):
            if self.status == 'A':
                atendimento = Atendimento.objects.create(
                    cidadao=self.cidadao,
                    agendamento=self,  # ✅ passa a instância de Agendamento
                    descricao=self.descricao,
                    status='P'
                )
                self.status = 'R'
                self.save()
                return atendimento
            return None

class Atendimento(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pendente'),
        ('R', 'Resolvido'),
        ('A', 'Em atendimento')
    ]

    cidadao=models.ForeignKey(Cidadao, on_delete=models.CASCADE, related_name='atendimento')
    agendamento=models.OneToOneField(Agendamento, on_delete=models.SET_NULL, null=True, blank=True, related_name='atendimento')
    descricao = models.TextField()
    decisoes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    data_atendimento=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Atendimento: {self.cidadao.nome} - {self.get_status_display()}'