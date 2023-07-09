# Generated by Django 4.2.2 on 2023-06-16 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroArma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_serie', models.CharField(max_length=8, verbose_name='NÚMERO DE SÉRIE')),
                ('modelo', models.IntegerField(choices=[(1, 'PT 100'), (2, 'SMT'), (3, 'CT')], verbose_name='MODELO')),
            ],
            options={
                'verbose_name': 'Cadastro de Arma',
                'verbose_name_plural': 'Cadastro de Armas',
            },
        ),
        migrations.CreateModel(
            name='CadastroCarregadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_serie', models.CharField(max_length=8, verbose_name='NÚMERO DE SÉRIE')),
                ('qtdcarreg', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], verbose_name='QUANTIDADE DE CARREGADORES')),
                ('qtdmunicao', models.IntegerField(choices=[(1, '15'), (2, '30')], verbose_name='QUANTIDADE DE MUNIÇÃO')),
            ],
            options={
                'verbose_name': 'Cadastro de Carregador',
                'verbose_name_plural': 'Cadastro de Carregadores',
            },
        ),
        migrations.CreateModel(
            name='CadastroColete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numerocad', models.CharField(max_length=20, verbose_name='NÚMERO DE SÉRIE')),
                ('fabricante', models.CharField(max_length=20, verbose_name='FABRICANTE')),
            ],
            options={
                'verbose_name': 'Cadastro de Colete',
                'verbose_name_plural': 'Cadastro de Coletes',
            },
        ),
    ]
