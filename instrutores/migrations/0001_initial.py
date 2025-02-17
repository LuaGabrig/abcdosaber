# Generated by Django 4.2.18 on 2025-02-11 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('titulo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrutores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rg', models.CharField(help_text='Rg', max_length=20)),
                ('nome', models.CharField(help_text='Nome', max_length=50)),
                ('dataNascimento', models.DateField(blank=True, help_text='Data de Nascimento', null=True)),
                ('telefone', models.CharField(help_text='Informe seu telefone:', max_length=9)),
                ('DDD', models.CharField(help_text='Informe o DDD', max_length=3)),
                ('data_registro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='titulo.titulo')),
            ],
        ),
    ]
