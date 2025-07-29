# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Arbitro(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arbitro'


class Equipo(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    total_jugadores = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipo'


class Estadio(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    ubicacion = models.CharField(max_length=100, blank=True, null=True)
    capacidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadio'


class Partido(models.Model):
    torneo = models.ForeignKey('Torneo', models.DO_NOTHING, blank=True, null=True)
    equipo_local = models.ForeignKey(Equipo, models.DO_NOTHING, blank=True, null=True)
    equipo_visitante = models.ForeignKey(Equipo, models.DO_NOTHING, related_name='partido_equipo_visitante_set', blank=True, null=True)
    estadio = models.ForeignKey(Estadio, models.DO_NOTHING, blank=True, null=True)
    arbitro = models.ForeignKey(Arbitro, models.DO_NOTHING, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partido'


class Torneo(models.Model):
    nombre = models.CharField(max_length=250, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'torneo'
