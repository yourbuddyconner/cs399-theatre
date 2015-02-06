from app.models import Show, Merchandise
from datetime import date
import django.db.utils

try: 
	if not Merchandise.objects.all():
		Merchandise.objects.create(
			name = "Marvin's Marvelous Cucumber Grab Bag",
			description = "So you can recreate the heartwarming occurances of 'Get These Cucumbers Off Of My Face', we're offering a special limited time grab bag of assorted cucumbers! Comes in a decorative burlap sack.",
			image = "/static/images/merchandise/cucumber.jpg",
			price = 999
		)
	if not Show.objects.all():
		Show.objects.create(
			name = "Get These Cucumbers Off Of My Face",
			description = "A heartwarming adventure, that will test the friendship of three best friends. In an alternate timeline, a masseuse, a hairdresser and a bank teller go on a crime spree.",
			image = "/static/images/shows/cucumber-mask.jpg",
			start_date = date(2015, 12, 24),
			end_date = date(2015, 1, 30),
			show_url = "/show1"
			)
		Show.objects.create(
			name = "The Thing: The 3D Experience",
			description = "Prepare yourself for the ultimate in 3D entertainment. Special visual effects take you into the world of everyone's favorite ball of hair!",
			image = "/static/images/shows/glasses-hair.jpg",
			start_date = date(2014, 12, 24),
			end_date = date(2015, 1, 30),
			show_url = "/show2"
			)
		Show.objects.create(
			name = "It Pays To Buy Good Tea",
			description = "From world-renownd British playwright, Gerrard Tea'n'Crumpets comes another amazing adaptation on the events of the infamous Boston Teaparty.",
			image = "/static/images/shows/it-pays-tea.jpg",
			start_date = date(2015, 3, 24),
			end_date = date(2016, 4, 5),
			show_url = "/show3"
			)
		Show.objects.create(
			name = "Sasquatch",
			description = "The sobering tale of the World's Most Ridiculously Hairy Man. A musical adaptation.",
			image = "/static/images/shows/sasquatch.jpg",
			start_date = date(2015, 4, 7),
			end_date = date(2016, 5, 25),
			show_url = "/show4"
			)
		Show.objects.create(
			name = "Yolo Swag: The Musical",
			description = "Too much yolo to handle.",
			image = "/media/images/shows/shows/80x80.gif",
			start_date = date(2015, 1, 24),
			end_date = date(2015, 3, 5),
			show_url = "/show5"
			)
		Show.objects.create(
			name = "Your Mom: The Saga Continues",
			description = "A touching tale of intrigue and passion.",
			image = "/static/images/shows/lady.jpg",
			start_date = date(2015, 2, 28),
			end_date = date(2015, 3, 5)
		)
		Show.objects.create(
			name = "Honey I Built A World-Dominating Robot",
			description = "A quirky family comedy about a lovable android named Norman and his lust for power.",
			image = "/static/images/shows/karate.jpg",
			start_date = date(2015, 1, 1),
			end_date = date(2015, 4, 30)
		)
		Show.objects.create(
			name = "True Stories: The Ballmer Peak",
			description = "A panel with the world's foremost computer scientists where they uncover the mysteries of drinking while coding.",
			image = "/media/images/shows/shows/80x80.gif",
			start_date = date(2015, 1, 31),
			end_date = date(2015, 1, 31)
		)
		Show.objects.create(
			name = "Salsa Dancing On Ice",
			description = "A special one-weekend salsa skating extravagnza!",
			image = "/media/images/shows/shows/80x80.gif",
			start_date = date(2015, 2, 5),
			end_date = date(2015, 2, 8)
		)
except django.db.utils.OperationalError: 
	pass