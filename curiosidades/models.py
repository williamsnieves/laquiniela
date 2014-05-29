from django.db import models,connection
from django.utils import timezone
import datetime 


# Create your models here.

class Curiosidad(models.Model):
	id = models.AutoField(primary_key=True)
	cod_mundial = models.CharField(max_length=10)
	copa = models.CharField(max_length=200)
	ano_mundial = models.IntegerField()
	pais_sede = models.CharField(max_length=200)
	cant_equipos = models.IntegerField()
	cant_partidos = models.IntegerField()
	cant_goles = models.IntegerField()
	promedio_goles = models.CharField(max_length=200)
	campeon = models.CharField(max_length=200)
	subcampeon = models.CharField(max_length=200)
	tercero = models.CharField(max_length=1000)
	cuarto = models.CharField(max_length=200)
	goleadores = models.CharField(max_length=200)
	max_goles = models.IntegerField()
	balon_oro = models.CharField(max_length=200)
	fairplay = models.CharField(max_length=200)
	descripcion = models.TextField(max_length=1000)
	curiosidad = models.CharField(max_length=255,default='')


	def __str__(self):
		return self.group_match