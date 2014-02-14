from django.db import models
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

	def __str__(self):
		return self.group_match
