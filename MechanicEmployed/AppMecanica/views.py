from django.shortcuts import render
from AppMecanica.models import *
from AppMecanica.forms import RegistroUsuario
from django.urls import reverse
from django.http import HttpResponseRedirect


def usuarioData(request):
    usuario =Usuario.objects.all()
    data={'usuario':usuario}
    return render(request,'appMecanica/listaUsuarios.html', data)
def registrarUsuario(request):
    form= RegistroUsuario()
    if request.method=='POST':
        form = RegistroUsuario(request.POST)
        if form.is_valid():
            print("Es valido")
            form.save()
            return HttpResponseRedirect(reverse("lista_usuarios"))
    data = {'form': form}
    return render (request,'appMecanica/formularioUsuario.html',data)