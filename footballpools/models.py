from django.db import models, connection
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.

class FootballPool(models.Model):
	id = models.AutoField(primary_key=True)
	cod_qnl = models.CharField(max_length=50)
	#user_qnl = models.ForeignKey('auth.User', related_name='quinielas')
	user_qnl = models.CharField(max_length=50)
	group_qnl = models.CharField(max_length=1)
	date_qnl = models.DateField()
	city_match = models.CharField(max_length=200,default='')
	name_qnl = models.CharField(max_length=200)
	team_a_qnl = models.CharField(max_length=3)
	goals_a_qnl = models.IntegerField()
	team_b_qnl = models.CharField(max_length=3)
	goals_b_qnl = models.IntegerField()
	result_qnl = models.CharField(max_length=5)
	flag_a_qnl = models.CharField(max_length=200,default='')
	flag_b_qnl = models.CharField(max_length=200,default='')
	order_qnl = models.CharField(max_length=200,default='')
	progress_qnl = models.CharField(max_length=6,default='')

	def __str__(self):
		return self.name_qnl

class ViewMatchesQnl:
	def getMatches(self):
		cursor = connection.cursor()
		cursor.execute("""
			SELECT * FROM vw_match_qnl
			""")
		matches_list = []
		finalmatches_list = []
		matches_dict = {}

		for row in cursor.fetchall():
			m = row
			matches_list.append(m)

		for i in range(len(matches_list)):
			matches_dict = dict(cod_qnl=matches_list[i][0],group_match=matches_list[i][1],date_match=matches_list[i][2].strftime("%Y-%m-%d"),name_match=matches_list[i][3],team_a_match=matches_list[i][4],
								jj=matches_list[i][5],jg=matches_list[i][6],je=matches_list[i][7],jp=matches_list[i][8],gf=matches_list[i][9],gc=matches_list[i][10],
								dif=matches_list[i][11],pts=matches_list[i][12])
			finalmatches_list.append(matches_dict)


		return finalmatches_list

class ViewPositionQnl:
	def  getPositions(self):
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM vw_position_qnl")
		position_list = []
		final_list = []
		position_dict = {}
		for row in cursor.fetchall():
			p = row
			position_list.append(p)

		for i in range(len(position_list)):
			position_dict = dict(cod_qnl=position_list[i][0],group=position_list[i][1],team=position_list[i][2],jj=position_list[i][3],jg=position_list[i][4],je=position_list[i][5],
									jp=position_list[i][6],gf=position_list[i][7],gc=position_list[i][8],dif=position_list[i][9],pts=position_list[i][10])
			final_list.append(position_dict)	

		return final_list
		
	def getPositionByGroup(self, group="", cod_qnl=None):
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM vw_position_qnl grupo WHERE grupo.group='"+group+"' AND grupo.cod_qnl='"+cod_qnl+"'")
		position_list = []
		final_list = []
		position_dict = {}

		for row in cursor.fetchall():
			p = row
			position_list.append(p)

		for i in range(len(position_list)):
			position_dict = dict(cod_qnl=position_list[i][0],group=position_list[i][1],team=position_list[i][2],jj=position_list[i][3],jg=position_list[i][4],je=position_list[i][5],
									jp=position_list[i][6],gf=position_list[i][7],gc=position_list[i][8],dif=position_list[i][9],pts=position_list[i][10])
			final_list.append(position_dict)


		return final_list





