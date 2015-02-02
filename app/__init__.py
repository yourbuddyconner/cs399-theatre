from app.models import Show
from datetime import date
import django.db.utils

try: 
	if not Show.objects.all():
		Show.objects.create(
			name = "Get These Cucumbers Off Of My Face",
			description = "A heartwarming adventure, that will test the friendship of three best friends. In an alternate timeline, a masseuse, a hairdresser and a bank teller go on a crime spree.",
			image = "/static/images/cucumber-mask.jpg",
			start_date = date(2015, 12, 24),
			end_date = date(2015, 1, 30)
			)
		Show.objects.create(
			name = "The Thing: The 3D Experience",
			description = "Prepare yourself for the ultimate in 3D entertainment. Special visual effects take you into the world of everyone's favorite ball of hair!",
			image = "/static/images/glasses-hair.jpg",
			start_date = date(2014, 12, 24),
			end_date = date(2015, 1, 30)
			)
		Show.objects.create(
			name = "It Pays To Buy Good Tea",
			description = "From world-renownd British playwright, Gerrard Tea'n'Crumpets comes another amazing adaptation on the events of the infamous Boston Teaparty.",
			image = "/static/images/it-pays-tea.jpg",
			start_date = date(2015, 3, 24),
			end_date = date(2016, 4, 5)
			)
		Show.objects.create(
			name = "Sasquatch",
			description = "The sobering tale of the World's Most Ridiculously Hairy Man. A musical adaptation.",
			image = "/static/images/sasquatch.jpg",
			start_date = date(2015, 4, 7),
			end_date = date(2016, 5, 25)
			)
		Show.objects.create(
			name = "Yolo Swag: The Musical",
			description = "Too much yolo to handle.",
			image = "/media/images/shows/80x80.gif",
			start_date = date(2015, 1, 24),
			end_date = date(2015, 3, 5)
			)
		Show.objects.create(
			name = "Your Mom: The Saga Continues",
			description = "A touching tale of intrigue and passion.",
			image = "/static/images/lady.jpg",
			start_date = date(2015, 2, 28),
			end_date = date(2015, 3, 5)
		)
		Show.objects.create(
			name = "Honey I Built A World-Dominating Robot",
			description = "A quirky family comedy about a lovable android named Norman and his lust for power.",
			image = "/static/images/karate.jpg",
			start_date = date(2015, 1, 1),
			end_date = date(2015, 4, 30)
		)
		Show.objects.create(
			name = "True Stories: The Ballmer Peak",
			description = "A panel with the world's foremost computer scientists where they uncover the mysteries of drinking while coding.",
			image = "/media/images/shows/80x80.gif",
			start_date = date(2015, 1, 31),
			end_date = date(2015, 1, 31)
		)
		Show.objects.create(
			name = "Salsa Dancing On Ice",
			description = "A special one-weekend salsa skating extravagnza!",
			image = "/media/images/shows/80x80.gif",
			start_date = date(2015, 2, 5),
			end_date = date(2015, 2, 8)
		)
except django.db.utils.OperationalError: 
	pass