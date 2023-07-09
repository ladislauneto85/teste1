from django.contrib import admin
from .models import Carga_Descarga
from .forms import CargaForm

@admin.register(Carga_Descarga)
class CargaDescargaAdmin(admin.ModelAdmin):
    form = CargaForm
    list_display = ('cad_matricula', 'patente', 'nomeguerra', 'armamento', 'carreg_1', 'placabalistica', 'observacao', 'senha', 'e_mail', 'data')
