# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from alunos.models import Alunos
# Create your views here.

def listar(request):
    lista_alunos = Alunos.objects.all()
    return HttpResponse(lista_alunos)