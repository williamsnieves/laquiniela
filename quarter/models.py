from django.db import models, connection
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.

class Quarter(models.Model):
	id = models.AutoField(primary_key=True)
	cod_qnl = models.CharField(max_length=50)
	cod_juego = models.CharField(max_length=5)
	cod_equipo = models.CharField(max_length=5)
	equipo = models.CharField(max_length=5)
	goles = models.IntegerField()
	clasificado = models.CharField(max_length=50)
	puntuacion = models.IntegerField()
	ruta = models.CharField(max_length=500)

	def __str__(self):
		return self.cod_qnl

class ViewCuartos:
	def getMatchesCuartos(self,cod_qnl=None):
		cursor = connection.cursor() 
		cursor.execute("SELECT * FROM vw_cuartos_qnl WHERE codquin='"+cod_qnl+"' ORDER BY 4")
		position_list = []
		final_list = []
		position_dict = {}

		for row in cursor.fetchall():
			p = row
			position_list.append(p)

		for i in range(len(position_list)):
			position_dict = dict(codquin=position_list[i][0],codjuego=position_list[i][1],cod_juego=position_list[i][2],equipo=position_list[i][3])
			final_list.append(position_dict)


		return final_list
