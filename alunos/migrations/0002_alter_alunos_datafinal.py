# Generated by Django 4.2.18 on 2025-02-22 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='dataFinal',
            field=models.DateField(help_text='Data Final', null=True),
        ),
    ]
