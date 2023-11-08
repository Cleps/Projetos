from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginDJ
from django.contrib.auth.decorators import login_required
import re

def checkEmail(s): # validando email
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex, s)):  
        return True
    else:  
        return False

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if len(senha) < 8 or len(senha) > 16:
            messages.info(request, 'A senha deve conter de 8 a 16 caracteres')
            return render(request, 'cadastro.html', {'username': username, 'email': email})
        
        if checkEmail(email) == False:
            messages.info(request, 'E-mail inválido')
            return render(request, 'cadastro.html', {'username': username, 'email': email})
        
        # checando caso nome seja repetido
        user = User.objects.filter(username = username).first()

        if user:
            messages.info(request, 'Usuario já cadastrado')
            return render(request, 'cadastro.html', {'username': username, 'email': email})
        
        # Adicione a mensagem de sucesso
        messages.success(request, 'Cadastrado com sucesso!')
        
        # criando usuário do database
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return redirect('login')

    

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        # autenticando
        user = authenticate(username = username, password = senha)

        if user:
            loginDJ(request, user) # logando no sistema

            return redirect('pagina_inicial') # Mandando pra pagina inicial
        else:
            messages.info(request, 'Usuario ou senha incorretos')
            return redirect('login')
        

# somente para testar ja que ainda não temos a aplicação, caso não esteja logado, ele redireciona para o login
# @login_required(login_url="/auth/login/")
# def aplicacao(request):
#     if request.user.is_authenticated:
#         return render(request, 'aplicacaotemporaria.html')
        
#     else:
#         return HttpResponse('Voce precisa estar logado')
    

