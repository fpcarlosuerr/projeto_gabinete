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