from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.

class FootballPool(models.Model):
	id = models.AutoField(primary_key=True)
	cod_qnl = models.CharField(max_length=3)
	user_qnl = models.ForeignKey(User)
	group_qnl = models.CharField(max_length=1)
	date_qnl = models.DateField()
	name_qnl = models.CharField(max_length=200)
	team_a_qnl = models.CharField(max_length=3)
	goals_a_qnl = models.IntegerField()
	team_b_qnl = models.CharField(max_length=3)
	goals_b_qnl = models.IntegerField()
	result_qnl = models.CharField(max_length=5)

	def __str__(self):
		return self.name_qnl



