from django.urls import path
from . import views

app_name = 'aluno'

urlpatterns = [
    path('listar/', views.listar, name="listar"),
]
