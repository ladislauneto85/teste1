from django import forms
from .models import CadastroSenha

class CadastroForm(forms.ModelForm):
    s_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CadastroSenha
        fields = ('s_name', 's_password')
