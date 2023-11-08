from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from .views import pagina_inicial, deletar_item, CriarListaView, CriarAtividadeView, CriarTarefaView, atualizar_item, atualizar_conteudo
from .views import atualizar_dados, ordenar_itens
urlpatterns = [
    path('', pagina_inicial, name='pagina_inicial'),
    path('criar_lista/', CriarListaView.as_view(), name='criar_lista'),
    path('criar_atividade/', CriarAtividadeView.as_view(), name='criar_atividade'),
    path('criar_tarefa/' , CriarTarefaView.as_view(), name='criar_tarefa'), 
    path('deletar_item/', deletar_item, name='deletar_item'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('atualizar_item/', atualizar_item, name='atualizar_item'),
    path('atualizar_conteudo/', atualizar_conteudo, name='atualizar_conteudo'),
    path('atualizar_dados/<str:object_type>/<int:item_id>/', atualizar_dados, name='atualizar_dados'),
    path('ordenar_itens/', ordenar_itens, name='ordenar_itens'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)