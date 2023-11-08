from django.test import TestCase
from django.contrib.auth.models import User
from lista.models import Lista
from atividade.models import Atividade

class AtividadeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.lista = Lista.objects.create(
            user=self.user,
            nome="Lista de Atividades",
            descricao="Descrição da Lista",
            dataInicio="2021-01-01",
            dataFim="2021-01-02",
            status=True,
            prioridade=1
        )

    def test_atividade_criacao(self):
        atividade = Atividade.objects.create(
            user=self.user,
            lista=self.lista,
            nome="Atividade Teste",
            descricao="Descrição da Atividade",
            dataInicio="2021-01-01",
            dataFim="2021-01-02",
            prioridade=1,
            status=True
        )
        self.assertEqual(atividade.nome, 'Atividade Teste')

    def test_atividade_prio(self):
        atividade = Atividade.objects.create(
            user=self.user,
            lista=self.lista,
            nome="Atividade Teste",
            descricao="Descrição da Atividade",
            dataInicio="2021-01-01",
            dataFim="2021-01-02",
            prioridade=2,
            status=True
        )
        self.assertEqual(atividade.prioridade, 2)