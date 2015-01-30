from app.models import Show
from datetime import date

if not Show.objects.all():
	print "Seeding dB!"
	Show(
		name = "Yolo Swag: The Musical",
		description = "Too much yolo to handle.",
		image = "/media/images/shows/80x80.gif",
		start_date = date(2015, 1, 24),
		end_date = date(2015, 3, 5)
		)
	Show.objects.create(
		name = "Your Mom: The Saga Continues",
		description = "A touching tale of intrigue and passion.",
		image = "/media/images/shows/80x80.gif",
		start_date = date(2015, 2, 28),
		end_date = date(2015, 3, 5)
	)
	Show.objects.create(
		name = "Honey I Built A World-Dominating Robot",
		description = "A quirky family comedy about a lovable android named Norman and his lust for power.",
		image = "/media/images/shows/80x80.gif",
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