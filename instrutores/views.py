# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from instrutores.models import Instrutores
# Create your views here.

def listar(request):
    lista_instrutores = Instrutores.objects.all()
    return HttpResponse(lista_instrutores)