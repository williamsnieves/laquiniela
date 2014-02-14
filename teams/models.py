from django.db import models
from django.utils import timezone
import datetime 

# Create your models here.

class Team(models.Model):
	id = models.AutoField(primary_key=True)
	name_team = models.CharField(max_length=200)
	country_team = models.CharField(max_length=200)
	confed_team = models.CharField(max_length=200)
	group_team = models.CharField(max_length=10)

	def __str__(self):
		return self.name_team
