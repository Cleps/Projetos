import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskpad_api.settings')  # Substitua "seu_projeto" pelo nome do seu projeto Django

# execute com python teste.py

import django
django.setup()

from lista.models import Lista
from atividade.models import Atividade

def criar_exemplos():
    # Criar uma lista de exemplo
    lista_exemplo2 = Lista.objects.create(
        nome='Minha Lista de Exemplo 2',
        descricao='Esta é uma lista de exemplo',
        dataInicio='2023-08-21',
        dataFim='2023-08-31',
        status=True,
        prioridade=2,
    )

    # Criar atividades de exemplo associadas à lista
    atividade1 = Atividade.objects.create(
        lista=lista_exemplo2,
        nome='Atividade 3',
        descricao='Esta é a atividade 1 de exemplo',
        dataInicio='2023-08-21',
        dataFim='2023-08-25',
        status=True,
        prioridade=1,
        texto='Texto da atividade 1',
    )

    atividade2 = Atividade.objects.create(
        lista=lista_exemplo2,
        nome='Atividade 4',
        descricao='Esta é a atividade 2 de exemplo',
        dataInicio='2023-08-26',
        dataFim='2023-08-31',
        status=False,
        prioridade=3,
        texto='Texto da atividade 2',
    )

    print('Exemplos de listas e atividades criados com sucesso!')

def criar_exemplos2():
    # Criar uma lista de exemplo
    lista_exemplo = Lista.objects.update(
        nome='Minha Lista de Exemplo 1',
        descricao='Esta é uma lista de exemplo',
        dataInicio='2023-08-21',
        dataFim='2023-08-31',
        status=True,
        prioridade=2,
        texto='Texto de texte da lista 1',
    )


    print('Exemplos de listas e atividades atualizad com sucesso!')

if __name__ == '__main__':
    criar_exemplos2()
