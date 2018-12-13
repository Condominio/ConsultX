from msilib.schema import ListView
from django.views.generic import ListView
from urllib import request
from django.shortcuts import render
#from Tools.pynche import ListViewer
from django.core.checks import templates
from django.shortcuts import render, redirect
#importar la url.py de Administrar Visitas
from apps.Administrar_Visitas.forms import PropietarioForm
from apps.Administrar_Visitas.models import Propietario

from django.http import HttpResponse

#FUNCION INDEX QUE LLAMA AL TEMPLATES -> Administrar_Visitas
def index(request):
    return render(request,'AdministrarVisitas/index.html')

#FUNCION PARA REGITRAR
def propietario_view(request):
    if request.method=='POST':
        form=PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Administrar_Visitas:index')
    else:
        form=PropietarioForm()
    return render(request, 'AdministrarVisitas/Propietario_form.html', {'form':form})

class propietario_list(ListView):
    model=Propietario
    template_name='AdministrarVisitas/Propietario_list.html'

