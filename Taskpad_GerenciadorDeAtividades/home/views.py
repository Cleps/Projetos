from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date
from ckeditor.fields import RichTextFormField
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiParameter
import logging
from lista.models import Lista
from atividade.models import Atividade
from tarefa.models import Tarefa
from .forms import ListaForm, AtividadeForm, TarefaForm
from django.views.decorators.csrf import csrf_protect
from docx import Document
from htmldocx import HtmlToDocx
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.core import serializers
from django.db.models import F, Case, When, Value, CharField, IntegerField

@login_required(login_url="/auth/login/")
def pagina_inicial(request):
    if request.user.is_authenticated:
        listas = Lista.objects.filter(user=request.user)
        atividades = Atividade.objects.filter(user=request.user)
        tarefas = Tarefa.objects.filter(user=request.user)
        texto_form = RichTextFormField()
        lista_form = ListaForm()
        atividade_form = AtividadeForm()
        tarefa_form = TarefaForm()

        return render(request, 'pagina_inicial.html', {
            'listas': listas,
            'atividades': atividades,
            'tarefas': tarefas,
            'lista_form': lista_form,
            'atividade_form': atividade_form,
            'tarefa_form': tarefa_form,
            'texto_form': texto_form, 
        })
    else:
        return HttpResponse('Você precisa estar logado')


def ordenar_itens(request):
    if request.method == 'POST':
        ordem = request.POST.get('ordenarPor')  # Obtém a opção selecionada no formulário
        print(ordem)

        listas = Lista.objects.filter(user=request.user)
        atividades = Atividade.objects.filter(user=request.user)
        tarefas = Tarefa.objects.filter(user=request.user)
        texto_form = RichTextFormField()
        lista_form = ListaForm()
        atividade_form = AtividadeForm()
        tarefa_form = TarefaForm()
        print(listas)
        # Adicione um campo virtual para ordenação
        if ordem == 'dataAsc':
            listas = sorted(listas, key=lambda x: x.dataInicio)
        elif ordem == 'dataDesc':
            listas = sorted(listas, key=lambda x: x.dataInicio, reverse=True)
        elif ordem == 'prioridadeAsc':
            listas = sorted(listas, key=lambda x: x.prioridade)
        elif ordem == 'prioridadeDesc':
            listas = sorted(listas, key=lambda x: x.prioridade, reverse=True)
        elif ordem == 'nomeAsc':
            listas = sorted(listas, key=lambda x: x.nome)
        elif ordem == 'nomeDesc':
            listas = sorted(listas, key=lambda x: x.nome, reverse=True)
        print('-------------------------------------------------------------------')
        print(listas)

        # Retorne apenas o conteúdo da div como resposta
        return render(request, 'listas.html', 
                    {'listas': listas, 
                    'atividades': atividades, 
                    'tarefas': tarefas,
                    'lista_form': lista_form,
                    'atividade_form': atividade_form,
                    'tarefa_form': tarefa_form,
                    'texto_form': texto_form, })
    return redirect('pagina_inicial')


@csrf_protect
def atualizar_conteudo(request):
    if request.method == "POST":
        object_type = request.POST.get('object_type')
        item_id = request.POST.get('object_id')
        conteudo_atividade = request.POST.get('conteudo_atividade')
        
        if object_type and item_id:
            if object_type == 'lista':
                obj = get_object_or_404(Lista, id=item_id)
                obj.texto = conteudo_atividade
                obj.save()
            elif object_type == 'atividade':
                obj = get_object_or_404(Atividade, id=item_id)
                obj.texto = conteudo_atividade
                obj.save()
            elif object_type == 'tarefa':
                obj = get_object_or_404(Tarefa, id=item_id)
                obj.texto = conteudo_atividade
                obj.save()

            # Se a exportação deve ser realizada
            exportar = request.POST.get('exportar')
            #print(exportar)
            if exportar == 'true':

                conteudo = obj.texto
                conteudo = processar_imagens_base64(conteudo) # chamando a função que fiz abaixo

                #print(obj.nome)
                #print(conteudo)
                nome_do_arquivo = f"{obj.nome}_exported.docx"

                #novo documento DOCX
                doc = Document()
                new_parser = HtmlToDocx()

                # conteúdo HTML p documento DOCX
                new_parser.add_html_to_document(conteudo, doc)

                # Salvar o documento DOCX em uma resposta HTTP para download
                response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                response['Content-Disposition'] = f'attachment; filename="{nome_do_arquivo}"'
                doc.save(response)

                return response
            
            return JsonResponse({'conteudo_atividade': obj.texto})

    return JsonResponse({'erro': 'Requisição inválida'})

# ----------------------------------------------------------------------
# Func para processar imagens em base64 que fiz nos documentos

import re
import base64
import tempfile

def processar_imagens_base64(conteudo_html):
    # Expressão regular para encontrar imagens em Base64 no conteúdo HTML
    padrao_img = r'<img .*?src="data:image\/(\w+);base64,([^"]+)"'
    matches = re.findall(padrao_img, conteudo_html)

    for formato, match in matches:
        imagem_binaria = base64.b64decode(match)

        # Determinar a extensão do arquivo com base no formato
        if formato == 'jpeg':
            extensao = 'jpg'
        elif formato == 'png':
            extensao = 'png'
        elif formato == 'gif':
            extensao = 'gif'
        else:
            # tratar outros formatos aqui
            extensao = 'jpg'

        # Salvando a imagem como um arquivo temporário
        with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{extensao}') as tmpfile:
            tmpfile.write(imagem_binaria)
            caminho_imagem_temporaria = tmpfile.name

        # Substitui a imagem pelo caminho do arquivo temporário no conteúdo HTML
        conteudo_html = conteudo_html.replace(f'data:image/{formato};base64,{match}', caminho_imagem_temporaria)

    return conteudo_html


# ----------------------------------------------------------------------
class CriarListaView(APIView):
    @extend_schema(
        description="Cria uma nova lista.",
        request=ListaForm,
        responses={201: "Objeto JSON contendo informações da nova lista criada."}
    )
    def post(self, request):
        nome_lista = request.data.get('nome')
        descricao = request.data.get('descricao')
        dataInicio = request.data.get('dataInicio')
        dataFim = request.data.get('dataFim')
        prioridade = request.data.get('prioridade')
        status = request.data.get('status')
        
        status = True if status == 'on' else False
        
        user = request.user

        if dataInicio:
            dataInicio = parse_date(dataInicio)
        else:
            dataInicio = None
        
        if dataFim:
            dataFim = parse_date(dataFim)
        else:
            dataFim = None

        nova_lista = Lista(
            user=user,
            nome=nome_lista,
            descricao=descricao,
            dataInicio=dataInicio,
            dataFim=dataFim,
            prioridade=prioridade,
            status=status
        )
        nova_lista.save()

        return redirect('pagina_inicial')

class CriarAtividadeView(APIView):
    @extend_schema(
        description="Cria uma nova atividade.",
        request=AtividadeForm,
        responses={201: "Objeto JSON contendo informações da nova atividade criada."}
    )
    def post(self, request):
        user = request.user
        lista_id = request.data.get('lista_id')
        nome_atividade = request.data.get('nome_atividade')
        descricao = request.data.get('descricao')
        dataInicio = request.data.get('dataInicio')
        dataFim = request.data.get('dataFim')
        status = request.data.get('status')
        prioridade = request.data.get('prioridade')

        status = True if status == 'on' else False
        
        if dataInicio:
            dataInicio = parse_date(dataInicio)
        else:
            dataInicio = None
        
        if dataFim:
            dataFim = parse_date(dataFim)
        else:
            dataFim = None

        nova_atividade = Atividade(
            user=user,
            lista_id=lista_id,
            nome=nome_atividade,
            descricao=descricao,
            dataInicio=dataInicio,
            dataFim=dataFim,
            status=status,
            prioridade=prioridade
        )
        nova_atividade.save()

        return redirect('pagina_inicial')

class CriarTarefaView(APIView):
    @extend_schema(
        description="Cria uma nova tarefa.",
        request=TarefaForm,
        responses={201: "Objeto JSON contendo informações da nova tarefa criada."}
    )
    def post(self, request):
        user = request.user
        atividade_id = request.data.get('atividade_id')
        nome_tarefa = request.data.get('nome_tarefa')
        descricao = request.data.get('descricao')
        dataInicio = request.data.get('dataInicio')
        dataFim = request.data.get('dataFim')
        status = request.data.get('status')
        prioridade = request.data.get('prioridade')

        status = True if status == 'on' else False
        
        if dataInicio:
            dataInicio = parse_date(dataInicio)
        else:
            dataInicio = None
        
        if dataFim:
            dataFim = parse_date(dataFim)
        else:
            dataFim = None
            
        nova_tarefa = Tarefa(
            user=user,
            atividade_id=atividade_id,
            nome=nome_tarefa,
            descricao=descricao,
            dataInicio=dataInicio,
            dataFim=dataFim,
            status=status,
            prioridade=prioridade
        )
        nova_tarefa.save()

        return redirect('pagina_inicial')

@api_view(['POST'])
@extend_schema(
    description="Deleta um item (lista, atividade ou tarefa).",
    parameters=[
        OpenApiParameter(name="objectType", type=str, location=OpenApiParameter.QUERY, description="Tipo de objeto (lista, atividade ou tarefa)."),
        OpenApiParameter(name="itemId", type=int, location=OpenApiParameter.QUERY, description="ID do item a ser excluído."),
    ],
    responses={200: "Redireciona para a página inicial após a exclusão do item."}
)
def deletar_item(request):
    if request.method == 'POST':
        objectType = request.data.get('objectType')
        itemId = request.data.get('itemId')

        if objectType and itemId:
            if objectType == 'lista':
                lista = get_object_or_404(Lista, id=itemId)
                for atividade in lista.atividade_set.all():
                    for tarefa in atividade.tarefa_set.all():
                        tarefa.delete()
                    atividade.delete()
                lista.delete()

            elif objectType == 'atividade':
                obj = get_object_or_404(Atividade, id=itemId)
                for tarefa in obj.tarefa_set.all():
                    tarefa.delete()
                obj.delete()

            elif objectType == 'tarefa':
                obj = get_object_or_404(Tarefa, id=itemId)
                obj.delete()

        return redirect('pagina_inicial')
    else:
        return redirect('pagina_inicial')





def atualizar_item(request):

    if request.method == "POST":
        object_type = request.POST.get('objectType')
        item_id = request.POST.get('itemId')
        # print(f'object_type: {object_type}')
        # print(f'item_id: {item_id}')
        if object_type and item_id:
            if object_type == 'lista':
                obj = get_object_or_404(Lista, id=item_id)
            elif object_type == 'atividade':
                obj = get_object_or_404(Atividade, id=item_id)
            elif object_type == 'tarefa':
                obj = get_object_or_404(Tarefa, id=item_id)

            dataInicio = request.POST.get('dataInicio')

            if dataInicio:
                dataInicio = parse_date(dataInicio)
            else:
                dataInicio = None

            dataFim = request.POST.get('dataFim')
            if dataFim:
                dataFim = parse_date(dataFim)
            else:
                dataFim = None

            obj.nome = request.POST.get('nome_tarefaatt')
            obj.descricao = request.POST.get('descricaoatt')
            obj.dataInicio = dataInicio

            obj.dataFim = dataFim
            obj.prioridade = request.POST.get('prioridadeatt')
            obj.save()
        
    return redirect('pagina_inicial')



def atualizar_dados(request, object_type, item_id):
    data = {}  # Crie um dicionário vazio para armazenar os dados a serem retornados

    if object_type == 'lista':
        # Se o tipo de objeto for uma lista, busque os dados da Lista
        lista = get_object_or_404(Lista, id=item_id)
        data['conteudo'] = lista.texto  # Supondo que o campo 'texto' contenha os dados que você deseja

    elif object_type == 'atividade':
        # Se o tipo de objeto for uma atividade, busque os dados da Atividade
        atividade = get_object_or_404(Atividade, id=item_id)
        data['conteudo'] = atividade.texto  # Supondo que o campo 'texto' contenha os dados que você deseja

    elif object_type == 'tarefa':
        # Se o tipo de objeto for uma tarefa, busque os dados da Tarefa
        tarefa = get_object_or_404(Tarefa, id=item_id)
        data['conteudo'] = tarefa.texto  # Supondo que o campo 'texto' contenha os dados que você deseja

    return JsonResponse(data)

'''
return render(request, 'pagina_inicial.html', {} Se for render, tu passa um template
return redirect('pagina_inicial') Se for redirect, tu passa uma função
'''