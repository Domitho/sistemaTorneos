from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Arbitro

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