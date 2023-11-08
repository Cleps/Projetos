from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Lista

class ViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_pagina_inicial(self):
        url = reverse('pagina_inicial')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pagina_inicial.html')

    def test_criar_lista(self):
        url = reverse('criar_lista')
        data = {
            'nome': 'Nova Lista',
            'descricao': 'Descrição da nova lista',
            'dataInicio': '2023-08-01',
            'dataFim': '2023-08-31',
            'prioridade': 2,
            'status': 'on',
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)

        nova_lista = Lista.objects.get(nome='Nova Lista')
        self.assertEqual(nova_lista.descricao, 'Descrição da nova lista')

    def tearDown(self):
        self.client.logout()
