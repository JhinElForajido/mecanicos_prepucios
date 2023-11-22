from django import forms 
from AppMecanica.models import *

class RegistroUsuario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad= forms.CharField()
    correo = forms.CharField()
    telefono= forms.CharField()

    nombre.widget.attrs['class']='form-control'
    apellido.widget.attrs['class']='form-control'
    edad.widget.attrs['class']='form-control'
    correo.widget.attrs['class']='form-control'
    telefono.widget.attrs['class']='form-control'
    class Meta:
        model=Usuario
        fields='__all__'
class RegistroUsuario(forms.ModelForm):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad= forms.CharField()
    correo = forms.CharField()
    telefono= forms.CharField()

    nombre.widget.attrs['class']='form-control'
    apellido.widget.attrs['class']='form-control'
    edad.widget.attrs['class']='form-control'
    correo.widget.attrs['class']='form-control'
    telefono.widget.attrs['class']='form-control'
    class Meta:
        model=Usuario
        fields='__all__'
