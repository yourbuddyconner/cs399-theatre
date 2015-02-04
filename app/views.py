from django.shortcuts import render
from app.models import Show, Merchandise


def home(request):
    return render(request, 'home.html', {'shows': Show.objects.all()})

def directions(request):
    return render(request, 'directions.html')

def merchandise(request):
    return render(request, 'merchandise.html', {'merchandise': Merchandise.objects.all()})

def tickets(request):
    return render(request, 'tickets.html')

def shows(request):
    return render(request, 'shows.html', {'shows': Show.objects.all()})
	
def giftcards(request):
    return render(request, 'giftcards.html')