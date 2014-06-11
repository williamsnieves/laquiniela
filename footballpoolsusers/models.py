from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.

class FootballPoolUser(models.Model):
	id = models.AutoField(primary_key=True)
	cod_qnl = models.CharField(max_length=50)
	#user_qnl = models.ForeignKey('auth.User', related_name='quinielas')
	username = models.CharField(max_length=50)
	qnl_fase = models.IntegerField(max_length=1,default=0)
	qnl_eliminatoria = models.IntegerField(max_length=1,default=0)