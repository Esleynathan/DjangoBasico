from django.shortcuts import render
from django.http import HttpResponse
import json

def cadastro(request):
    # nome = request.GET.get('nome')    
    # sobrenome = request.GET.get('sobrenome')    
    # idade = request.GET.get('idade')

    erro = request.GET.get('erro')  
    
    return render(request, ('cadastro/index.html'), {'erro': erro})
    # {'nome': nome, 'sobrenome': sobrenome, 'idade':idade})

def valida_formulario(request):
    nome = request.GET.get('nome')
    email = request.GET.get('email')
    return HttpResponse(json.dumps({'nome':nome, 'email': email}))