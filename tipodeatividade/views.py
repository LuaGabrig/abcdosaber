from django.shortcuts import render
from django.http import HttpResponse

from tipodeatividade.models import TipoDeAtividade

# Create your views here.

def index (request):
    return HttpResponse("<!DOCType='html'><html><body><p>Olá, estou no App 'Tipo De Atividade'</p></body></html>")

def listar(request):
    lista_tipodeatividade = TipoDeAtividade.objects.all()
    resposta = "<ul>"
    for tipodeatividade in lista_tipodeatividade:
        resposta+= '<li>{0}</li>'.format(tipodeatividade.descricao)
        
        resposta+= '</ul>'
        print(resposta)
    return HttpResponse(resposta)

def detalhe_tipodeatividade(request, ta_codigo):
    tipodeatividade = TipoDeAtividade.objects.get(pk=ta_codigo)
    return HttpResponse(tipodeatividade)