# Generated by Django 4.2.2 on 2023-06-18 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('policial', '0002_alter_cadastrosenha_s_password'),
        ('cargadescarga', '0002_alter_carga_descarga_senha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carga_descarga',
            name='senha',
            field=models.ForeignKey(max_length=150, on_delete=django.db.models.deletion.CASCADE, to='policial.cadastrosenha', verbose_name='SENHA'),
        ),
    ]
