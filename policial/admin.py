from django.contrib import admin
from .forms import CadastroForm
from .models import CadastroPolicial, CadastroSenha, CadastroEmail

@admin.register(CadastroSenha)
class SenhaAdmin(admin.ModelAdmin):
    form = CadastroForm
    list_display = ('s_name', 's_password')

@admin.register(CadastroPolicial)
class PolicialAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome')

@admin.register(CadastroEmail)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'primeiro_nome')

