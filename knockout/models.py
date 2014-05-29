from django.db import models, connection
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.

class Knockout(models.Model):
	id = models.AutoField(primary_key=True)
	cod_qnl = models.CharField(max_length=50)
	cod_juego = models.CharField(max_length=5)
	cod_equipo = models.CharField(max_length=5)
	equipo = models.CharField(max_length=5)
	goles = models.IntegerField()
	clasificado = models.CharField(max_length=50)
	puntuacion = models.IntegerField()
	ruta = models.CharField(max_length=500)
	progress_octavos = models.CharField(max_length=6,default='')

	def __str__(self):
		return self.cod_qnl

class ViewOctavos:
	def getMatchesOctavos(self,cod_qnl=None):
		cursor = connection.cursor() 
		cursor.execute("SELECT * FROM vw_octavos_qnl WHERE cod_qnl='"+cod_qnl+"' ORDER BY 4")
		position_list = []
		final_list = []
		position_dict = {}

		for row in cursor.fetchall():
			p = row
			position_list.append(p)

		for i in range(len(position_list)):
			position_dict = dict(cod_qnl=position_list[i][0],grupo=position_list[i][1],team=position_list[i][2],juego=position_list[i][3],clas=position_list[i][4])
			final_list.append(position_dict)


		return final_list