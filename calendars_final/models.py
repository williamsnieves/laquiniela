from django.db import models, connection
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.

class CalendarFinal(models.Model):
	id = models.AutoField(primary_key=True)
	cod_juego = models.CharField(max_length=5)
	cod_equipo = models.CharField(max_length=5)
	equipo = models.CharField(max_length=5)
	goles = models.IntegerField()
	clasificado = models.CharField(max_length=50)
	ruta = models.CharField(max_length=500)

	def __str__(self):
		return self.cod_equipo