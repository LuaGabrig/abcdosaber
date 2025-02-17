from django.urls import path, include
from . import views

urlpatterns = [
    
    path('nome/', views.nome, name='nome'),
    path('lista/', views.listar, name='listar'),
    path('bomdia/',views.show_mensagem, name='bomdia'),
    path('<int:ta_codigo>/', views.detalhe_tipodeatividade, name='tipodeatividade')

]