from django.shortcuts import render
from django.http import HttpResponse
import json

from .models import Pessoa, Cargos

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro/index.html')

    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')        
        senha = request.POST.get('senha')
        pessoa = Pessoa(nome = nome,
                        email = email,
                        senha = senha
                        )

        pessoa.save()

        return HttpResponse('Você foi cadastrado.')

def listar(request):
    # if len(request.GET) != 0:
    #     nome = request.GET.get('nome')
    #     email = request.GET.get('email')
    #     senha = request.GET.get('senha')

    #     cargo = Cargos.objects.get(id=1)

    #     pessoa = Pessoa(nome = nome,
    #                     email = email,
    #                     senha = senha,
    #                     cargo = cargo)
    #     pessoa.save()

    pessoas = Pessoa.objects.filter(nome = 'esley')
    pessoas.delete()


    pessoas = Pessoa.objects.all()
    return render(request, 'listar/listar.html', {'pessoas': pessoas})
    
    # ?nome=erika&email=erika@e.com&senha=senha1