from django.shortcuts import render
from django.http import HttpResponse
from familiares.models import Familiares

# Create your views here.
def crear_familiar(request, nombre, apellido, edad, parentesco, vivo):
    #nuevo_familiar = Familiares.objects.create(nombre='Mary',apellido='Antúnez',edad=70,parentesco='madre',vivo=True)
    vivo_bool = True
    if vivo == 'S':
        vivo_bool = False
    nuevo_familiar = Familiares.objects.create(nombre=nombre,apellido=apellido,edad=edad,parentesco=parentesco,vivo=vivo_bool)
    print(nuevo_familiar)
    return HttpResponse('Se creó el nuevo familiar')

def listar_familiares(request):
    todos_los_familiares = Familiares.objects.all()
    print(todos_los_familiares)
    for familiar in todos_los_familiares:
        print(familiar.apellido)
    context = {
        'todos_los_familiares':todos_los_familiares,
        }
    return render(request, 'listar_familiares.html', context=context)