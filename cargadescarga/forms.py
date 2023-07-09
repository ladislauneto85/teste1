from django import forms
from .models import Carga_Descarga

class CargaForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Carga_Descarga
        fields = ('cad_matricula', 'patente', 'nomeguerra', 'armamento', 'carreg_1', 'placabalistica', 'observacao', 'senha', 'e_mail')
