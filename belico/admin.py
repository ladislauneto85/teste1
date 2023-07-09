from django.contrib import admin
from .models import CadastroArma, CadastroCarregadores, CadastroColete

@admin.register(CadastroArma)
class CadastroBelicoAdmin(admin.ModelAdmin):
    list_display = ('numero_serie', 'modelo')

@admin.register(CadastroCarregadores)
class CadastroBelicoAdmin(admin.ModelAdmin):
    list_display = ('num_serie', 'qtdcarreg', 'qtdmunicao')

@admin.register(CadastroColete)
class CadastroBelicoAdmin(admin.ModelAdmin):
    list_display = ('numerocad', 'fabricante')

