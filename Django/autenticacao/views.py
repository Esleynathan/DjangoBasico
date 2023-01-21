from django.shortcuts import render
from django.http import HttpResponse
import json

from .models import Pessoa

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
    pessoa = Pessoa.objects.filter(nome = 'Ésley NathanGomes Barbosa').filter(senha = 'senha1')[0]
    pessoa.delete()
    
    pessoas = Pessoa.objects.all()
    return render(request, 'listar/listar.html', {'pessoas': pessoas})