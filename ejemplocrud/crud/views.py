from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import crud
from .forms import crudForm
# Create your views here.

def prueba(request):
    return render(request, 'paginas/prueba.html')

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def cruds(request):
    leerCruds = crud.objects.all()
    #print(leerCruds)
    return render(request, 'crud/index.html', {'cruds': leerCruds})

def crear(request):
    formulario = crudForm(request.POST or None,  request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect ('crud')
    return render(request, 'crud/crear.html', {'formulario': formulario})

def editar(request, id):
    elemento = crud.objects.get(id=id)
    formulario = crudForm(request.POST or None,  request.FILES or None, instance=elemento)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('crud')
    return render(request, 'crud/editar.html', {'formulario': formulario})

def eliminar(request, id):
    elemento = crud.objects.get(id=id)
    elemento.delete()
    return redirect ('crud')