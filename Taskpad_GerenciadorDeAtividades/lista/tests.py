from django.test import TestCase
from django.contrib.auth.models import User
from lista.models import Lista

class ListaTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_criar_lista(self):
        lista = Lista.objects.create(
            user=self.user,
            nome="Lista de Teste",
            descricao="Descrição da Lista",
            dataInicio="2021-01-01",
            dataFim="2021-01-02",
            status=True,
            prioridade=1
        )
        self.assertEqual(lista.nome, 'Lista de Teste')

    def test_prioridade_lista(self):
        lista = Lista.objects.create(
            user=self.user,
            nome="Lista de Teste",
            descricao="Descrição da Lista",
            dataInicio="2021-01-01",
            dataFim="2021-01-02",
            status=True,
            prioridade=2
        )
        self.assertEqual(lista.prioridade, 2)

    def test_lista_vazia(self):
        lista = Lista.objects.create(
            user=self.user,
            nome="Lista Vazia",
            descricao="Descrição da Lista Vazia",
            dataInicio="2021-01-01",
            dataFim="2021-01-02",
            status=False,
            prioridade=3
        )
        self.assertFalse(lista.status)
        self.assertEqual(lista.atividade_set.count(), 0)