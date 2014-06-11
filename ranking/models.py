from django.db import models, connection
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.

class Ranking(models.Model):
	id = models.AutoField(primary_key=True)
	cod_qnl = models.CharField(max_length=50)
	pts_goala = models.IntegerField()
	pts_goalb = models.IntegerField()
	pts_results = models.IntegerField()
	pts_winner = models.IntegerField()
	points_total = models.IntegerField()

	def __str__(self):
		return self.points_total

class ViewRanking:
	def  getRanking(self):
		cursor = connection.cursor()
		cursor.execute("SELECT cod_qnl, pts_goal_a, pts_goal_b, pts_result, pts_winner, points FROM vw_sumpoints_qnl LIMIT 10")
		position_list = []
		final_list = []
		position_dict = {}
		for row in cursor.fetchall():
			p = row
			position_list.append(p)

		for i in range(len(position_list)):
			position_dict = dict(cod_qnl=position_list[i][0],pts_goal_a=position_list[i][1],pts_goal_b=position_list[i][2],pts_result=position_list[i][3],pts_winner=position_list[i][4],
									points=position_list[i][5])
			final_list.append(position_dict)	

		return final_list
