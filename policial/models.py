from django.db import models
from django.contrib.auth.hashers import make_password

# Importe a classe que apresentará um erro de validação
from django.core.exceptions import ValidationError

# Crie um método para validar o valor informado
def validate_matricula(value):
    if not value.isdigit():
        raise ValidationError('Deve conter apenas números')
    
class CadastroPolicial(models.Model):
    
    matricula = models.CharField('MATRÍCULA', max_length=8, validators=[validate_matricula])
    nome = models.CharField('NOME COMPLETO', max_length=50)
        
    def __str__(self):
        return str(self.matricula)

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'


class CadastroSenha(models.Model):

    s_name = models.CharField('NOME DE GUERRA', max_length=50, null=False)
    s_password = models.CharField(verbose_name='SENHA', max_length=150, null=False)

    def save(self, *args, **kwargs):
        self.s_password = make_password(self.s_password)
        super(CadastroSenha, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.s_password)

    class Meta:
        verbose_name = 'Acesso'
        verbose_name_plural = 'Acessos'


class CadastroEmail(models.Model):

    email = models.EmailField('E-MAIL', max_length=50, null=False)
    primeiro_nome = models.CharField('Primeiro nome', max_length=20, null=False)

    def __str__(self):
        return str(self.email)
    
    class Meta:
        verbose_name = 'E-mail'
        verbose_name_plural = 'E-mails'

