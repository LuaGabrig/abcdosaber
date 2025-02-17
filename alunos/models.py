from django.db import models
from django.urls import reverse

class Alunos(models.Model):
    """Modelo representando um Alunos"""
    
    matricula = models.AutoField(primary_key=True)
    
    nome = models.CharField(max_length=20, help_text='Nome')
        
    dataInicial = models.DateField(null=False, help_text='Data Inicial')
    
    dataFinal = models.DateField(help_text='Data Final')

    
    def _str_(self):
        return f' {self.matricula} - {self.nome} - {self.dataInicial} - {self.dataFinal}'