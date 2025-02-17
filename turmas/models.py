from django.db import models
from django.urls import reverse
from django.utils import timezone


from tipodeatividade.models import TipoDeAtividade
from alunos.models import Alunos
from instrutores.models import Instrutores


"""Modelo representando um Turmas"""

class Turma(models.Model):
    numero = models.AutoField(primary_key=True, help_text="Informe a turma do Aluno")
    horario_aula = models.TimeField(help_text="Informe a hora em que a hora da aula da Turma")
    duracao_aula = models.SmallIntegerField(default=30, help_text="Informe a duração da aula da Turma")
    data_inicial = models.DateField(default=timezone.now(), help_text="Informe a data inicial da Turma")    
    data_final = models.DateField(null=True, blank=True, help_text="Informe a data final da Turma")
    codigo_atividade = models.ForeignKey(TipoDeAtividade, on_delete=models.CASCADE)
    matricula_monitor = models.ForeignKey(Alunos, null=True, blank=True, on_delete=models.SET_NULL)
    id_instrutor = models.ForeignKey(Instrutores, null=True, on_delete=models.CASCADE)

    
    class Meta:
        ordering = ['numero']
    
    def _str_(self):
        return f'Turma:{self.numero} - Instrutor:{self.id_instrutor.nome} - Monitor:{self.matricula_monitor.nome}'


class TurmaAluno(models.Model):
    numero_turma = models.ForeignKey(Turma, on_delete=models.CASCADE, help_text="Turma do aluno.")
    matricula_aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE, help_text="Matrícula do aluno.")
    data_inicio_matricula = models.DateField(null=False, default=timezone.now(),help_text="Data da matrícula do aluno.")
    data_fim_matricula= models.DateField(null=True, blank=True, help_text="Data fim de matrícula do aluno.")
    
    def _str_(self):
        resposta = f' Turma:{self.numero_turma} - Aluno:{self.matricula_aluno} '
              
        return resposta
    
class Ausencia(models.Model):
    numero_turma = models.ForeignKey(Turma, on_delete=models.CASCADE, help_text="Turma do aluno.")
    matricula_aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE, help_text="Matrícula do aluno.")
    data_ausencia = models.DateField(null=False, default=timezone.now(),help_text="Data da falta do aluno.")
    
    def _str_(self):
        resposta = f' Turma:{self.numero_turma} - Aluno:{self.matricula_aluno} - Ausencia:{self.data_ausencia.strftime("%d/%m/%y")}'
        return resposta