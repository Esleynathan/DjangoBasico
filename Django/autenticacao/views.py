from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    pessoa = [{'nome': 'Ésley Nathan', 'idade': '20','profissao': 'Programador'},
    {'nome': 'Outro Esley', 'idade': '21','profissao': 'Escritor'}
    ]
    return render(request, ('cadastro/index.html'),
    {'pessoa': pessoa})