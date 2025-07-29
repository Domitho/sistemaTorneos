from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Arbitro, Equipo, Estadio, Partido, Torneo

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

## ESTADIOS ##

def listar_estadios(request):
    estadios = Estadio.objects.all()
    return render(request, 'estadio/listar_estadio.html', {'estadios': estadios})

def form_nuevo_estadio(request):
    return render(request, 'estadio/nuevo_estadio.html')

def guardar_estadio(request):
    Estadio.objects.create(
        nombre=request.POST['nombre'],
        ubicacion=request.POST['ubicacion'],
        capacidad=request.POST['capacidad']
    )
    messages.success(request, 'Estadio registrado correctamente.')
    return redirect('listar_estadios')

def form_editar_estadio(request, id):
    estadio = Estadio.objects.get(id=id)
    return render(request, 'estadio/editar_estadio.html', {'estadio': estadio})

def actualizar_estadio(request, id):
    estadio = Estadio.objects.get(id=id)
    estadio.nombre = request.POST['nombre']
    estadio.ubicacion = request.POST['ubicacion']
    estadio.capacidad = request.POST['capacidad']
    estadio.save()
    messages.success(request, 'Estadio actualizado correctamente.')
    return redirect('listar_estadios')

def eliminar_estadio(request, id):
    estadio = Estadio.objects.get(id=id)
    estadio.delete()
    messages.success(request, 'Estadio eliminado correctamente.')
    return redirect('listar_estadios')


## TORNEOS ##

def listar_torneos(request):
    torneos = Torneo.objects.all()
    return render(request, 'torneo/listar_torneo.html', {'torneos': torneos})

def form_nuevo_torneo(request):
    return render(request, 'torneo/nuevo_torneo.html')

def guardar_torneo(request):
    Torneo.objects.create(
        nombre=request.POST['nombre'],
        fecha_inicio=request.POST['fecha_inicio'],
        fecha_fin=request.POST['fecha_fin']
    )
    messages.success(request, 'Torneo registrado correctamente.')
    return redirect('listar_torneos')

def form_editar_torneo(request, id):
    torneo = Torneo.objects.get(id=id)
    return render(request, 'torneo/editar_torneo.html', {'torneo': torneo})

def actualizar_torneo(request, id):
    torneo = Torneo.objects.get(id=id)
    torneo.nombre = request.POST['nombre']
    torneo.fecha_inicio = request.POST['fecha_inicio']
    torneo.fecha_fin = request.POST['fecha_fin']
    torneo.save()
    messages.success(request, 'Torneo actualizado correctamente.')
    return redirect('listar_torneos')

def eliminar_torneo(request, id):
    torneo = Torneo.objects.get(id=id)
    torneo.delete()
    messages.success(request, 'Torneo eliminado correctamente.')
    return redirect('listar_torneos')


## PARTIDOS ##

def listar_partidos(request):
    partidos = Partido.objects.all()
    return render(request, 'partido/listar_partido.html', {'partidos': partidos})

def form_nuevo_partido(request):
    torneos = Torneo.objects.all()
    equipos = Equipo.objects.all()
    estadios = Estadio.objects.all()
    arbitros = Arbitro.objects.all()
    return render(request, 'partido/nuevo_partido.html', {
        'torneos': torneos,
        'equipos': equipos,
        'estadios': estadios,
        'arbitros': arbitros
    })

def guardar_partido(request):
    Partido.objects.create(
        torneo_id=request.POST['torneo'],
        equipo_local_id=request.POST['equipo_local'],
        equipo_visitante_id=request.POST['equipo_visitante'],
        estadio_id=request.POST['estadio'],
        arbitro_id=request.POST['arbitro'],
        fecha=request.POST['fecha'],
        hora=request.POST['hora']
    )
    messages.success(request, 'Partido registrado correctamente.')
    return redirect('listar_partidos')

def form_editar_partido(request, id):
    partido = Partido.objects.get(id=id)
    torneos = Torneo.objects.all()
    equipos = Equipo.objects.all()
    estadios = Estadio.objects.all()
    arbitros = Arbitro.objects.all()
    return render(request, 'partido/editar_partido.html', {
        'partido': partido,
        'torneos': torneos,
        'equipos': equipos,
        'estadios': estadios,
        'arbitros': arbitros
    })

def actualizar_partido(request, id):
    partido = Partido.objects.get(id=id)
    partido.torneo_id = request.POST['torneo']
    partido.equipo_local_id = request.POST['equipo_local']
    partido.equipo_visitante_id = request.POST['equipo_visitante']
    partido.estadio_id = request.POST['estadio']
    partido.arbitro_id = request.POST['arbitro']
    partido.fecha = request.POST['fecha']
    partido.hora = request.POST['hora']
    partido.save()
    messages.success(request, 'Partido actualizado correctamente.')
    return redirect('listar_partidos')

def eliminar_partido(request, id):
    partido = Partido.objects.get(id=id)
    partido.delete()
    messages.success(request, 'Partido eliminado correctamente.')
    return redirect('listar_partidos')
