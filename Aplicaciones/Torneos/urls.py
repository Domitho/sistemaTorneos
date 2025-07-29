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
    path('arbitros/eliminar/<int:id>/', views.eliminar_arbitro, name='eliminar_arbitro')
]
