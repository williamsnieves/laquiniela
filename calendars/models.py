from django.db import models,connection
from django.utils import timezone
import datetime 


# Create your models here.

class Calendar(models.Model):
	id = models.AutoField(primary_key=True)
	group_match = models.CharField(max_length=10)
	cod_match = models.CharField(max_length=200)
	date_match = models.DateField()
	city_match = models.CharField(max_length=200)
	name_match = models.CharField(max_length=200)
	team_a_match = models.CharField(max_length=200)
	goals_a_match = models.IntegerField()
	team_b_match = models.CharField(max_length=200)
	goals_b_match = models.IntegerField()
	result_match = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	flag_a_match = models.CharField(max_length=200,default='/')
	flag_b_match = models.CharField(max_length=200,default='/')

	def __str__(self):
		return self.group_match

class ViewMatches:
	def getMatches(self):
		cursor = connection.cursor()
		cursor.execute("""
			SELECT * FROM vw_matches
			""")
		matches_list = []
		finalmatches_list = []
		matches_dict = {}

		for row in cursor.fetchall():
			m = row
			matches_list.append(m)

		for i in range(len(matches_list)):
			matches_dict = dict(group_match=matches_list[i][0],cod_match=matches_list[i][1],date_match=matches_list[i][2],name_match=matches_list[i][3],team_a_match=matches_list[i][4],
								jj=matches_list[i][5],jg=matches_list[i][6],je=matches_list[i][7],jp=matches_list[i][7],gf=matches_list[i][9],gc=matches_list[i][10],
								dif=matches_list[i][11],pts=matches_list[i][12])
			finalmatches_list.append(matches_dict)


		return finalmatches_list

class ViewPosition:
	def  getPositions(self):
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM vw_positiontab")
		position_list = []
		final_list = []
		position_dict = {}
		for row in cursor.fetchall():
			p = row
			position_list.append(p)

		for i in range(len(position_list)):
			position_dict = dict(group=position_list[i][0],team=position_list[i][1],jj=position_list[i][2],jg=position_list[i][3],je=position_list[i][4],
									jp=position_list[i][5],gf=position_list[i][6],gc=position_list[i][7],dif=position_list[i][8],pts=position_list[i][9])
			final_list.append(position_dict)	

		return final_list
		
	def getPositionByGroup(self, group=""):
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM vw_positiontab grupo WHERE grupo.group='"+group+"'")
		position_list = []
		final_list = []
		position_dict = {}

		for row in cursor.fetchall():
			p = row
			position_list.append(p)

		for i in range(len(position_list)):
			position_dict = dict(group=position_list[i][0],team=position_list[i][1],jj=position_list[i][2],jg=position_list[i][3],je=position_list[i][4],
									jp=position_list[i][5],gf=position_list[i][6],gc=position_list[i][7],dif=position_list[i][8],pts=position_list[i][9])
			final_list.append(position_dict)


		return final_list
