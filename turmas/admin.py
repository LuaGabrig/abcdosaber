from django.contrib import admin
from turmas.models import Turma
from turmas.models import TurmaAluno, Ausencia


# Register your models here.

admin.site.register(Turma)

admin.site.register(TurmaAluno)

admin.site.register(Ausencia)