from django.shortcuts import render
from app.models import Show, Merchandise


def home(request):
    return render(request, 'home.html', {
    	'slideshow_items': Show.objects.all()
    })

def directions(request):
    return render(request, 'directions.html',{
    	'shows': Show.objects.all()
    })

def merchandise(request):
    return render(request, 'merchandise.html', {
    	'merchandise': Merchandise.objects.all(),
    	'slideshow_items': Show.objects.all() 
    	})

def tickets(request):
    return render(request, 'tickets.html',{
    	'slideshow_items': Show.objects.all()
    })

def shows(request):
    return render(request, 'shows.html', {
    	'slideshow_items': Show.objects.all()
    })
	
def giftcards(request):
    return render(request, 'giftcards.html',{
    	'slideshow_items': Show.objects.all()
    })