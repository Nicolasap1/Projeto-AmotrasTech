from django import forms
from .models import Cadastro_Usuario

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistroForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    senha_confirmacao = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Cadastro_Usuario
        fields = ('email', 'name', 'password')