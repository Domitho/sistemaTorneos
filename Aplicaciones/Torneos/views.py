from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Arbitro, Equipo, Estadio, Partido, Torneo
from django.db import connection
from datetime import datetime
from datetime import date, time
import re
from django.db.models import Q





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
    nombre = request.POST['nombre'].strip()
    apellido = request.POST['apellido'].strip()
    edad_str = request.POST['edad'].strip()

    if not nombre.replace(" ", "").isalpha():
        messages.error(request, 'El nombre solo debe contener letras.')
        return redirect('nuevo_arbitro')

    if not apellido.replace(" ", "").isalpha():
        messages.error(request, 'El apellido solo debe contener letras.')
        return redirect('nuevo_arbitro')

    if not edad_str.isdigit():
        messages.error(request, 'La edad debe ser un número.')
        return redirect('nuevo_arbitro')

    edad = int(edad_str)
    if edad < 18 or edad > 50:
        messages.error(request, 'La edad debe estar entre 18 y 50 años.')
        return redirect('nuevo_arbitro')


    Arbitro.objects.create(nombre=nombre, apellido=apellido, edad=edad)
    messages.success(request, 'Árbitro registrado correctamente')
    return redirect('listar_arbitros')

def editar_arbitro(request, id):
    arbitro = Arbitro.objects.get(id=id)
    return render(request, 'arbitro/editar_arbitro.html', {'arbitro': arbitro})

def actualizar_arbitro(request, id):
    arbitro = Arbitro.objects.get(id=id)
    nombre = request.POST['nombre'].strip()
    apellido = request.POST['apellido'].strip()
    edad_str = request.POST['edad'].strip()

   
    if not nombre.replace(" ", "").isalpha():
        messages.error(request, 'El nombre solo debe contener letras.')
        return redirect('editar_arbitro', id=id)

    if not apellido.replace(" ", "").isalpha():
        messages.error(request, 'El apellido solo debe contener letras.')
        return redirect('editar_arbitro', id=id)

    if not edad_str.isdigit():
        messages.error(request, 'La edad debe ser un número.')
        return redirect('editar_arbitro', id=id)

    edad = int(edad_str)
    if edad < 18 or edad > 50:
        messages.error(request, 'La edad debe estar entre 18 y 50 años.')
        return redirect('editar_arbitro', id=id)

    
    arbitro.nombre = nombre
    arbitro.apellido = apellido
    arbitro.edad = edad
    arbitro.save()
    messages.success(request, 'Árbitro actualizado correctamente')
    return redirect('listar_arbitros')

def eliminar_arbitro(request, id):
    arbitro = Arbitro.objects.get(id=id)
    arbitro.delete()
    messages.success(request, 'Árbitro eliminado correctamente')
    return redirect('listar_arbitros')




# EQUIPOS

def listar_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipo/listar_equipo.html', {'equipos': equipos})


def form_nuevo_equipo(request):
    return render(request, 'equipo/nuevo_equipo.html')


def guardar_equipo(request):
    nombre = request.POST['nombre'].strip()
    descripcion = request.POST['descripcion'].strip()
    total_str = request.POST['total_jugadores'].strip()

    # Validar nombre: letras, números y espacios
    if not re.fullmatch(r'[A-Za-zÁÉÍÓÚáéíóúÑñ0-9 ]+', nombre):
        messages.error(request, "El nombre solo debe contener letras, números y espacios.")
        return redirect('form_nuevo_equipo')

    # Validar número de jugadores
    if not total_str.isdigit():
        messages.error(request, "El total de jugadores debe ser un número.")
        return redirect('form_nuevo_equipo')

    total = int(total_str)
    if total < 6 or total > 15:
        messages.error(request, "El total de jugadores debe estar entre 6 y 15.")
        return redirect('form_nuevo_equipo')

    # Si todo está correcto, guardar
    Equipo.objects.create(nombre=nombre, descripcion=descripcion, total_jugadores=total)
    messages.success(request, 'Equipo registrado correctamente.')
    return redirect('listar_equipos')


def form_editar_equipo(request, id):
    equipo = Equipo.objects.get(id=id)
    return render(request, 'equipo/editar_equipo.html', {'equipo': equipo})


def actualizar_equipo(request, id):
    equipo = Equipo.objects.get(id=id)
    nombre = request.POST['nombre'].strip()
    descripcion = request.POST['descripcion'].strip()
    total_str = request.POST['total_jugadores'].strip()

    # Validar nombre: letras, números y espacios
    if not re.fullmatch(r'[A-Za-zÁÉÍÓÚáéíóúÑñ0-9 ]+', nombre):
        messages.error(request, "El nombre solo debe contener letras, números y espacios.")
        return redirect('form_editar_equipo', id=id)

    # Validar número de jugadores
    if not total_str.isdigit():
        messages.error(request, "El total de jugadores debe ser un número.")
        return redirect('form_editar_equipo', id=id)

    total = int(total_str)
    if total < 6 or total > 15:
        messages.error(request, "El total de jugadores debe estar entre 6 y 15.")
        return redirect('form_editar_equipo', id=id)

    # Guardar cambios
    equipo.nombre = nombre
    equipo.descripcion = descripcion
    equipo.total_jugadores = total
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
    nombre = request.POST['nombre'].strip()
    ubicacion = request.POST['ubicacion'].strip()
    capacidad_str = request.POST['capacidad'].strip()

    # Validar nombre (letras, números y espacios)
    if not re.fullmatch(r'[A-Za-zÁÉÍÓÚáéíóúÑñ0-9 ]+', nombre):
        messages.error(request, "El nombre solo debe contener letras, números y espacios.")
        return redirect('form_nuevo_estadio')

    # Validar ubicación (solo letras y espacios)
    if not re.fullmatch(r'[A-Za-zÁÉÍÓÚáéíóúÑñ ]+', ubicacion):
        messages.error(request, "La ubicación solo debe contener letras y espacios.")
        return redirect('form_nuevo_estadio')

    # Validar capacidad
    if not capacidad_str.isdigit():
        messages.error(request, "La capacidad debe ser un número.")
        return redirect('form_nuevo_estadio')

    capacidad = int(capacidad_str)
    if capacidad < 1 or capacidad > 700:
        messages.error(request, "La capacidad debe estar entre 1 y 700.")
        return redirect('form_nuevo_estadio')

    Estadio.objects.create(nombre=nombre, ubicacion=ubicacion, capacidad=capacidad)
    messages.success(request, 'Estadio registrado correctamente.')
    return redirect('listar_estadios')


def form_editar_estadio(request, id):
    estadio = Estadio.objects.get(id=id)
    return render(request, 'estadio/editar_estadio.html', {'estadio': estadio})


def actualizar_estadio(request, id):
    estadio = Estadio.objects.get(id=id)
    nombre = request.POST['nombre'].strip()
    ubicacion = request.POST['ubicacion'].strip()
    capacidad_str = request.POST['capacidad'].strip()

    # Validar nombre (letras, números y espacios)
    if not re.fullmatch(r'[A-Za-zÁÉÍÓÚáéíóúÑñ0-9 ]+', nombre):
        messages.error(request, "El nombre solo debe contener letras, números y espacios.")
        return redirect('form_editar_estadio', id=id)

    # Validar ubicación (solo letras y espacios)
    if not re.fullmatch(r'[A-Za-zÁÉÍÓÚáéíóúÑñ ]+', ubicacion):
        messages.error(request, "La ubicación solo debe contener letras y espacios.")
        return redirect('form_editar_estadio', id=id)

    # Validar capacidad
    if not capacidad_str.isdigit():
        messages.error(request, "La capacidad debe ser un número.")
        return redirect('form_editar_estadio', id=id)

    capacidad = int(capacidad_str)
    if capacidad < 1 or capacidad > 700:
        messages.error(request, "La capacidad debe estar entre 1 y 700.")
        return redirect('form_editar_estadio', id=id)

    estadio.nombre = nombre
    estadio.ubicacion = ubicacion
    estadio.capacidad = capacidad
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
    nombre = request.POST['nombre'].strip()
    fecha_inicio_str = request.POST['fecha_inicio']
    fecha_fin_str = request.POST['fecha_fin']

    # Validar nombre
    if not nombre.replace(" ", "").isalpha():
        messages.error(request, "El nombre solo debe contener letras y espacios.")
        return redirect('form_nuevo_torneo')

    # Validar formato de fechas
    try:
        fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d").date()
        fecha_fin = datetime.strptime(fecha_fin_str, "%Y-%m-%d").date()
    except ValueError:
        messages.error(request, "Formato de fecha inválido.")
        return redirect('form_nuevo_torneo')

    hoy = datetime.today().date()
    anio_actual = hoy.year

    # Validar rango de fecha_inicio
    if fecha_inicio < hoy or fecha_inicio.year != anio_actual:
        messages.error(request, "La fecha de inicio debe ser desde hoy en adelante y dentro del año actual.")
        return redirect('form_nuevo_torneo')

    # Validar fecha_fin
    if fecha_fin <= fecha_inicio or fecha_fin.year != anio_actual:
        messages.error(request, "La fecha de fin debe ser posterior a la de inicio y dentro del año actual.")
        return redirect('form_nuevo_torneo')

    # Si pasa todo, guardar
    Torneo.objects.create(
        nombre=nombre,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin
    )
    messages.success(request, 'Torneo registrado correctamente.')
    return redirect('listar_torneos')

def form_editar_torneo(request, id):
    torneo = Torneo.objects.get(id=id)
    return render(request, 'torneo/editar_torneo.html', {'torneo': torneo})

def actualizar_torneo(request, id):
    torneo = Torneo.objects.get(id=id)
    nombre = request.POST['nombre'].strip()
    fecha_inicio_str = request.POST['fecha_inicio']
    fecha_fin_str = request.POST['fecha_fin']

    # Validar nombre
    if not nombre.replace(" ", "").isalpha():
        messages.error(request, "El nombre solo debe contener letras y espacios.")
        return redirect('form_editar_torneo', id=id)

    try:
        fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d").date()
        fecha_fin = datetime.strptime(fecha_fin_str, "%Y-%m-%d").date()
    except ValueError:
        messages.error(request, "Formato de fecha inválido.")
        return redirect('form_editar_torneo', id=id)

    hoy = datetime.today().date()
    anio_actual = hoy.year

    if fecha_inicio < hoy or fecha_inicio.year != anio_actual:
        messages.error(request, "La fecha de inicio debe ser desde hoy en adelante y dentro del año actual.")
        return redirect('form_editar_torneo', id=id)

    if fecha_fin <= fecha_inicio or fecha_fin.year != anio_actual:
        messages.error(request, "La fecha de fin debe ser posterior a la de inicio y dentro del año actual.")
        return redirect('form_editar_torneo', id=id)

    torneo.nombre = nombre
    torneo.fecha_inicio = fecha_inicio
    torneo.fecha_fin = fecha_fin
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
    torneo_id = request.POST['torneo']
    equipo_local_id = request.POST['equipo_local']
    equipo_visitante_id = request.POST['equipo_visitante']
    estadio_id = request.POST['estadio']
    arbitro_id = request.POST['arbitro']
    fecha = request.POST['fecha']
    hora = request.POST['hora']

    hoy = date.today()
    fin_anio = date(hoy.year, 12, 31)
    hora_min = time(8, 0)
    hora_max = time(19, 0)

    if equipo_local_id == equipo_visitante_id:
        messages.error(request, 'El equipo local y visitante no pueden ser el mismo.')
        return redirect('form_nuevo_partido')

    if not (hoy <= date.fromisoformat(fecha) <= fin_anio):
        messages.error(request, 'La fecha debe estar entre hoy y el 31 de diciembre.')
        return redirect('form_nuevo_partido')

    if not (hora_min <= time.fromisoformat(hora) <= hora_max):
        messages.error(request, 'La hora debe estar entre 08:00 y 19:00.')
        return redirect('form_nuevo_partido')

    if Partido.objects.filter(
        equipo_local_id=equipo_local_id,
        equipo_visitante_id=equipo_visitante_id
    ).exists():
        messages.error(request, 'Ya existe un partido entre estos dos equipos.')
        return redirect('form_nuevo_partido')

    if Partido.objects.filter(
        fecha=fecha
    ).filter(
        Q(equipo_local_id=equipo_local_id) |
        Q(equipo_visitante_id=equipo_local_id) |
        Q(equipo_local_id=equipo_visitante_id) |
        Q(equipo_visitante_id=equipo_visitante_id)
    ).exists():
        messages.error(request, 'Uno de los equipos ya tiene partido ese día.')
        return redirect('form_nuevo_partido')

    if Partido.objects.filter(estadio_id=estadio_id, fecha=fecha, hora=hora).exists():
        messages.error(request, 'El estadio ya está reservado en esa fecha y hora.')
        return redirect('form_nuevo_partido')

    Partido.objects.create(
        torneo_id=torneo_id,
        equipo_local_id=equipo_local_id,
        equipo_visitante_id=equipo_visitante_id,
        estadio_id=estadio_id,
        arbitro_id=arbitro_id,
        fecha=fecha,
        hora=hora
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

    torneo_id = request.POST['torneo']
    equipo_local_id = request.POST['equipo_local']
    equipo_visitante_id = request.POST['equipo_visitante']
    estadio_id = request.POST['estadio']
    arbitro_id = request.POST['arbitro']
    fecha = request.POST['fecha']
    hora = request.POST['hora']

    hoy = date.today()
    fin_anio = date(hoy.year, 12, 31)
    hora_min = time(8, 0)
    hora_max = time(19, 0)

    if equipo_local_id == equipo_visitante_id:
        messages.error(request, 'El equipo local y visitante no pueden ser el mismo.')
        return redirect('form_editar_partido', id=id)

    if not (hoy <= date.fromisoformat(fecha) <= fin_anio):
        messages.error(request, 'La fecha debe estar entre hoy y el 31 de diciembre.')
        return redirect('form_editar_partido', id=id)

    if not (hora_min <= time.fromisoformat(hora) <= hora_max):
        messages.error(request, 'La hora debe estar entre 08:00 y 19:00.')
        return redirect('form_editar_partido', id=id)

    if Partido.objects.filter(
        equipo_local_id=equipo_local_id,
        equipo_visitante_id=equipo_visitante_id
    ).exclude(id=id).exists():
        messages.error(request, 'Ya existe un partido entre estos dos equipos.')
        return redirect('form_editar_partido', id=id)

    if Partido.objects.filter(
        fecha=fecha
    ).filter(
        Q(equipo_local_id=equipo_local_id) |
        Q(equipo_visitante_id=equipo_local_id) |
        Q(equipo_local_id=equipo_visitante_id) |
        Q(equipo_visitante_id=equipo_visitante_id)
    ).exclude(id=id).exists():
        messages.error(request, 'Uno de los equipos ya tiene partido ese día.')
        return redirect('form_editar_partido', id=id)

    if Partido.objects.filter(estadio_id=estadio_id, fecha=fecha, hora=hora).exclude(id=id).exists():
        messages.error(request, 'El estadio ya está reservado en esa fecha y hora.')
        return redirect('form_editar_partido', id=id)

    partido.torneo_id = torneo_id
    partido.equipo_local_id = equipo_local_id
    partido.equipo_visitante_id = equipo_visitante_id
    partido.estadio_id = estadio_id
    partido.arbitro_id = arbitro_id
    partido.fecha = fecha
    partido.hora = hora
    partido.save()

    messages.success(request, 'Partido actualizado correctamente.')
    return redirect('listar_partidos')


def eliminar_partido(request, id):
    partido = Partido.objects.get(id=id)
    partido.delete()
    messages.success(request, 'Partido eliminado correctamente.')
    return redirect('listar_partidos')



## DASHBOARDS ##

def estadisticas_torneos(request):
    datos = {}

    with connection.cursor() as cursor:
        # 1. Partidos por torneo
        cursor.execute("""
            SELECT t.nombre, COUNT(p.id)
            FROM partido p
            JOIN torneo t ON p.torneo_id = t.id
            GROUP BY t.nombre;
        """)
        datos['partidos_por_torneo'] = cursor.fetchall()

        # 2. Equipos por descripción
        cursor.execute("""
            SELECT descripcion, COUNT(*) FROM equipo GROUP BY descripcion;
        """)
        datos['equipos_por_descripcion'] = cursor.fetchall()

        # 3. Partidos por estadio
        cursor.execute("""
            SELECT e.nombre, COUNT(p.id)
            FROM partido p
            JOIN estadio e ON p.estadio_id = e.id
            GROUP BY e.nombre;
        """)
        datos['partidos_por_estadio'] = cursor.fetchall()

        # 4. Promedio de edad de árbitros
        cursor.execute("""
            SELECT ROUND(AVG(edad)) FROM arbitro;
        """)
        datos['promedio_edad_arbitros'] = cursor.fetchone()[0]

        # 5. Top 2 equipos por jugadores
        cursor.execute("""
            SELECT nombre, total_jugadores
            FROM equipo
            ORDER BY total_jugadores DESC
            LIMIT 2;
        """)
        datos['top_equipos'] = cursor.fetchall()

        # 6. Árbitros con más partidos dirigidos
        cursor.execute("""
            SELECT a.nombre || ' ' || a.apellido, COUNT(p.id)
            FROM partido p
            JOIN arbitro a ON p.arbitro_id = a.id
            GROUP BY a.nombre, a.apellido
            ORDER BY COUNT(p.id) DESC
            LIMIT 5;
        """)
        datos['partidos_por_arbitro'] = cursor.fetchall()

        # 7. Fechas con más partidos
        cursor.execute("""
            SELECT fecha, COUNT(*) FROM partido GROUP BY fecha ORDER BY COUNT(*) DESC LIMIT 5;
        """)
        datos['partidos_por_fecha'] = cursor.fetchall()

        # 8. Equipos enfrentados
        cursor.execute("""
            SELECT el.nombre, ev.nombre, COUNT(p.id)
            FROM partido p
            JOIN equipo el ON p.equipo_local_id = el.id
            JOIN equipo ev ON p.equipo_visitante_id = ev.id
            GROUP BY el.nombre, ev.nombre;
        """)
        datos['duelos_equipos'] = cursor.fetchall()

        # 9. Partidos por mes
        cursor.execute("""
            SELECT TO_CHAR(fecha, 'YYYY-MM'), COUNT(*)
            FROM partido
            GROUP BY TO_CHAR(fecha, 'YYYY-MM')
            ORDER BY TO_CHAR(fecha, 'YYYY-MM');
        """)
        datos['partidos_por_mes'] = cursor.fetchall()

        # 10. Estadios con más partidos
        cursor.execute("""
            SELECT e.nombre, COUNT(p.id)
            FROM partido p
            JOIN estadio e ON p.estadio_id = e.id
            GROUP BY e.nombre
            ORDER BY COUNT(p.id) DESC
            LIMIT 5;
        """)
        datos['estadios_top'] = cursor.fetchall()

    return render(request, 'dashboard/estadisticas.html', datos)
