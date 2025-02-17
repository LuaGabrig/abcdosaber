from django.db import models
from django.urls import reverse

# Modelo representando um Tipo de Atividade
class Titulo(models.Model):
    """Modelo representando um Tipo de Atividade"""
    codigo = models.AutoField(primary_key=True,
                                 help_text='Código do Titulo')
    descricao = models.CharField(max_length=100, null=False,
                                 help_text='Informe a descrição do Titulo')

    def _str_(self):
        return f'{self.codigo} - {self.descricao}'