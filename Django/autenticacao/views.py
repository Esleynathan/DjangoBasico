from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    # nome = request.GET.get('nome')    
    # sobrenome = request.GET.get('sobrenome')    
    # idade = request.GET.get('idade')

    erro = request.GET.get('erro')  
    
    return render(request, ('cadastro/index.html'), {'erro': erro})
    # {'nome': nome, 'sobrenome': sobrenome, 'idade':idade})