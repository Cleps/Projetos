from django.urls import path
from . import views
from django.contrib.auth import views as views_auth

urlpatterns = [
    #path('', views.aplicacao, name ='aplicacao'), # definindo a pagina principal de login
    path('cadastro/', views.cadastro, name ='cadastro'),
    path('login/', views.login, name='login'),
    path('logout/', views_auth.LogoutView.as_view(), name='logout'), # para fazer logout
    #path('aplicacao/', views.aplicacao, name='aplicacao' )
    ]