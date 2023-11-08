from django.db import models
from lista.models import Lista
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Atividade(models.Model):

    CHOICES = (
        (1, 'Baixa'),
        (2, 'Média'),
        (3, 'Alta'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE, default=1)  # Chave estrangeira para Lista
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    dataInicio = models.DateField(null=True, blank=True)
    dataFim = models.DateField(null=True, blank=True)
    status = models.BooleanField()
    prioridade = models.IntegerField(choices=CHOICES) #Aqui é IntegerField
    texto = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.nome
