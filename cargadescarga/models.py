from django.db import models
from policial.models import CadastroPolicial, CadastroSenha, CadastroEmail
from belico.models import CadastroArma, CadastroCarregadores, CadastroColete
from django.contrib.auth.hashers import make_password

class Carga_Descarga(models.Model):

    PATENTE_CHOICES = [
        (1, 'CEL'),
        (2, 'TEN CEL'),
        (3, 'MAJ'),
        (4, 'CAP'),
        (5, 'TEN'),
        (6, 'ASP'),
        (7, 'SUB TEN'),
        (8, 'SGT'),
        (9, 'CB'),
        (10, 'SD'),
        (11, 'AL SD'),
    ]

    cad_matricula = models.ForeignKey(CadastroPolicial, on_delete=models.CASCADE, verbose_name='MATRÍCULA')
    patente = models.IntegerField(verbose_name='POSTO/GRADUAÇÃO', choices=PATENTE_CHOICES)
    nomeguerra = models.CharField('NOME DE GUERRA', max_length=15)
    armamento = armamento = models.ForeignKey(CadastroArma, on_delete=models.CASCADE, verbose_name='ARMA')
    carreg_1 = models.ForeignKey(CadastroCarregadores, on_delete=models.CASCADE, verbose_name='CARREGADOR 1')    
    placabalistica = models.ForeignKey(CadastroColete, on_delete=models.CASCADE, verbose_name='COLETE')
    observacao = models.CharField('OBSERVAÇÃO', max_length=50)    
    senha = models.ForeignKey(CadastroSenha, on_delete=models.CASCADE, verbose_name='SENHA', max_length=150, null=False)
    e_mail = models.ForeignKey(CadastroEmail, on_delete=models.CASCADE, verbose_name='E-MAIL')
    data = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.senha = make_password(self.senha)
        super(Carga_Descarga, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.cad_matricula)
    
    class Meta:
        verbose_name = 'Carga_Descarga'
        verbose_name_plural = 'Cargas_Descargas'

