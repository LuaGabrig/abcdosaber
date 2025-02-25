# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from titulo.models import Titulo
from titulo.forms import TituloForm

# Create your views here.

def listar(request):
    lista_titulo = Titulo.objects.all()
    contexto = {
        'titulo': lista_titulo
    }
    
    return render (request, 'tirulo/listarTitulo.html', context=contexto)

def carregar_cadastro(request):
    return render (request, 'titulo/cadastrarTitulo.html')

def cadastrar(request):
    form= TituloForm(request.POST)
    if form.is_valid():
        dados_titulo = form.cleaned_data
        tirulo = Titulo (
            descricao = dados_titulo['descricao']
        )
        
        Titulo.save()
        
        return render(request, 'titulo/cadastrarTitulo.html')
    
    