from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Arbitro, Equipo

# VISTA PRINCIPAL
def home(request):
    return render(request, 'home.html')

# ARBITROS

def listar_arbitros(request):
    arbitros = Arbitro.objects.all()
    return render(request, 'arbitro/listar_arbitro.html', {'arbitros': arbitros})

def nuevo_arbitro(request):
    return render(request, 'arbitro/nuevo_arbitro.html')

def guardar_arbitro(request):
    Arbitro.objects.create(
        nombre=request.POST['nombre'],
        apellido=request.POST['apellido'],
        edad=request.POST['edad'],
    )

    messages.success(request, 'Arbitro Registrado Correctamente')
    return redirect('listar_arbitros')

def editar_arbitro(request, id):
    arbitro = Arbitro.objects.get(id=id)
    return render(request, 'arbitro/editar_arbitro.html', {'arbitro': arbitro})

def actualizar_arbitro(request, id):
    arbitro = Arbitro.objects.get(id=id)
    arbitro.nombre = request.POST['nombre']
    arbitro.apellido = request.POST['apellido']
    arbitro.edad = request.POST['edad']
    arbitro.save()
    messages.success(request, 'Arbitro Actualizado Correctamente')
    return redirect('listar_arbitros')

def eliminar_arbitro(request, id):
    arbitro = Arbitro.objects.get(id=id)
    arbitro.delete()
    messages.success(request, 'Arbitro Eliminado Correctamente')
    return redirect('listar_arbitros')

## EQUIPOS ##

def listar_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipo/listar_equipo.html', {'equipos': equipos})

def form_nuevo_equipo(request):
    return render(request, 'equipo/nuevo_equipo.html')

def guardar_equipo(request):
    Equipo.objects.create(
        nombre=request.POST['nombre'],
        descripcion=request.POST['descripcion'],
        total_jugadores=request.POST['total_jugadores']
    )
    messages.success(request, 'Equipo registrado correctamente.')
    return redirect('listar_equipos')

def form_editar_equipo(request, id):
    equipo = Equipo.objects.get(id=id)
    return render(request, 'equipo/editar_equipo.html', {'equipo': equipo})

def actualizar_equipo(request, id):
    equipo = Equipo.objects.get(id=id)
    equipo.nombre = request.POST['nombre']
    equipo.descripcion = request.POST['descripcion']
    equipo.total_jugadores = request.POST['total_jugadores']
    equipo.save()
    messages.success(request, 'Equipo actualizado correctamente.')
    return redirect('listar_equipos')

def eliminar_equipo(request, id):
    equipo = Equipo.objects.get(id=id)
    equipo.delete()
    messages.success(request, 'Equipo eliminado correctamente.')
    return redirect('listar_equipos')
