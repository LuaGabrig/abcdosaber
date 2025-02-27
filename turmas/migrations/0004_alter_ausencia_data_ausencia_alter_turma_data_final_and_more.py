# Generated by Django 4.2.18 on 2025-02-15 00:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0003_alter_turma_options_alter_turma_data_final_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ausencia',
            name='data_ausencia',
            field=models.DateField(default=datetime.datetime(2025, 2, 15, 0, 32, 17, 427674, tzinfo=datetime.timezone.utc), help_text='Data da falta do aluno.'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='data_final',
            field=models.DateField(blank=True, help_text='Informe a data final da Turma', null=True),
        ),
        migrations.AlterField(
            model_name='turma',
            name='data_inicial',
            field=models.DateField(default=datetime.datetime(2025, 2, 15, 0, 32, 17, 427674, tzinfo=datetime.timezone.utc), help_text='Informe a data inicial da Turma'),
        ),
        migrations.AlterField(
            model_name='turmaaluno',
            name='data_inicio_matricula',
            field=models.DateField(default=datetime.datetime(2025, 2, 15, 0, 32, 17, 427674, tzinfo=datetime.timezone.utc), help_text='Data da matrícula do aluno.'),
        ),
    ]
