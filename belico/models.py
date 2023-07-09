from django.db import models

class CadastroArma(models.Model):
    
    MODELO_CHOICES = [
        (1, 'PT 100'),
        (2, 'SMT'),
        (3, 'CT'),  
    ]
        
    numero_serie = models.CharField('NÚMERO DE SÉRIE', max_length=8)
    modelo = models.IntegerField(verbose_name='MODELO', choices=MODELO_CHOICES)

    def __str__(self):
        return str(self.numero_serie)
    
    class Meta:
        verbose_name = 'Cadastro de Arma'
        verbose_name_plural = 'Cadastro de Armas'


class CadastroCarregadores(models.Model):

    QTD_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
    ]

    QTDMUNICAO_CHOICES = [
        (1, '15'),
        (2, '30'),
    ]

    num_serie = models.CharField('NÚMERO DE SÉRIE', max_length=8)
    qtdcarreg = models.IntegerField(verbose_name='QUANTIDADE DE CARREGADORES', choices=QTD_CHOICES)
    qtdmunicao = models.IntegerField(verbose_name='QUANTIDADE DE MUNIÇÃO', choices=QTDMUNICAO_CHOICES)

    def __str__(self):
        return str(self.num_serie)
    
    class Meta:
        verbose_name = 'Cadastro de Carregador'
        verbose_name_plural = 'Cadastro de Carregadores'


class CadastroColete(models.Model):

    numerocad = models.CharField('NÚMERO DE SÉRIE', max_length=20)
    fabricante = models.CharField('FABRICANTE', max_length=20)

    def __str__(self):
        return str(self.numerocad)
    
    class Meta:
        verbose_name = 'Cadastro de Colete'
        verbose_name_plural = 'Cadastro de Coletes'


