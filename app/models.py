from django.db import models
from app import fake
from django.utils import timezone
import datetime

class Show(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	start_date = models.DateField('day the show begins')
	end_date = models.DateField('day the show ends')
	
	# returns a friendly name for django
	def __unicode__(self):
		return self.name

	def isPlayingCurrently(self):
		return self.end_date <= datetime.date.today()

class Ticket(models.Model):
	show = models.ForeignKey(Show)
	price = models.DecimalField(decimal_places=2, max_digits=5)
	
	# returns a friendly name for django
	def __unicode__(self):             
		return str(self.show.name) + ": $" + str(self.price)