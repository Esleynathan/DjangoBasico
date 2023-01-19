from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    return HttpResponse('Faça seu cadastro')

def auth(request):
    return HttpResponse('Você esta na autenticacao')