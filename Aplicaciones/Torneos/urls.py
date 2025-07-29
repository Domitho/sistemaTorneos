from django.urls import path
from . import views

urlpatterns = [
    # HOME
    path('home/', views.home),

    # ARBITROS
    path('arbitros/', views.listar_arbitros, name='listar_arbitros'),
    path('arbitros/nuevo/', views.nuevo_arbitro, name='nuevo_arbitro'),
    path('arbitros/guardar/', views.guardar_arbitro, name='guardar_arbitro'),
    path('arbitros/editar/<int:id>/', views.editar_arbitro, name='editar_arbitro'),
    path('arbitros/actualizar/<int:id>/', views.actualizar_arbitro, name='actualizar_arbitro'),
    path('arbitros/eliminar/<int:id>/', views.eliminar_arbitro, name='eliminar_arbitro'),

    # EQUIPOS
    path('equipos/', views.listar_equipos, name='listar_equipos'),
    path('equipos/nuevo/', views.form_nuevo_equipo, name='form_nuevo_equipo'),
    path('equipos/guardar/', views.guardar_equipo, name='guardar_equipo'),
    path('equipos/editar/<int:id>/', views.form_editar_equipo, name='form_editar_equipo'),
    path('equipos/actualizar/<int:id>/', views.actualizar_equipo, name='actualizar_equipo'),
    path('equipos/eliminar/<int:id>/', views.eliminar_equipo, name='eliminar_equipo'),

]
