from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    nome = 'Ésley Nathan'
    idade = '20'
    profissao = 'Programador'
    return render(request, ('cadastro/index.html'),
    {'nome': nome, 'idade': idade, 'profissao': profissao})