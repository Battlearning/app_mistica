from django import forms
from .models import Cliente, Producto, Categoria
from django.contrib.auth.forms import AuthenticationForm


class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.IntegerField()
    email=  forms.EmailField()

class Registro_Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

class Inicio_Sesion_Form(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)


class Buscar_Producto_Form(forms.Form):
    nombre = forms.CharField(label="Buscar Producto", max_length=100)

class Buscar_Categoria_Form(forms.Form):
    nombre = forms.CharField(label="Buscar Categoría", max_length=100)