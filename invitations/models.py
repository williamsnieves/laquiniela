from django.db import models, connection
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.

class Invitation(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=50)
	invitacion = models.CharField(max_length=4,default='')

	def __str__(self):
		return self.username