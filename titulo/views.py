# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from titulo.models import Titulo

# Create your views here.

def listar(request):
    lista_titulo = Titulo.objects.all()
    contexto = {
        'titulo': lista_titulo
    }
    
    return render (request, 'tirulo/listarTitulo.html', context=contexto)

