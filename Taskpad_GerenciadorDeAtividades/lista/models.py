from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Agora Lista, Atividade e Tarefa tem comportamentos quase iguais pois os mesmos podem ser editados como arquivos de texto
class Lista(models.Model):
    CHOICES = (
        (1, 'Baixa'),
        (2, 'Média'),
        (3, 'Alta'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    dataInicio = models.DateField(null=True, blank=True)
    dataFim = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=True)
    prioridade = models.IntegerField(choices=CHOICES) 
    texto = RichTextField(null=True, blank=True)
    
    def __str__(self):
        return self.nome
   
