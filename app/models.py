from django.db import models
from django.utils import timezone
from app.settings import MEDIA_ROOT
import datetime

class Show(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	image = models.ImageField(upload_to='images/shows', default='static/images/placehold_square.gif')
	start_date = models.DateField('day the show begins')
	end_date = models.DateField('day the show ends')
	show_url = models.CharField(max_length=100, default='/')
	
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

class Merchandise(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	image = models.ImageField(upload_to='images/shows', default='static/images/placehold_square.gif')
	price = models.IntegerField(default=0)

	# returns a friendly name for django
	def __unicode__(self):             
		return str(self.name) + ": $" + str(self.price)