from django.shortcuts import render
from app.models import Show, Merchandise


def home(request):
    return render(request, 'home.html', {
    	'shows': Show.objects.all(),
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
    	'shows': Show.objects.all(),
    	'slideshow_items': Show.objects.all()
    })

def shows(request):
    return render(request, 'shows.html', {
    	'shows': Show.objects.all(),
    	'slideshow_items': Show.objects.all()
    })
	
def giftcards(request):
    return render(request, 'giftcards.html',{
    	'slideshow_items': Show.objects.all()
    })

def show1(request):
    return render(request, 'show1.html',{
        'slideshow_items': Show.objects.all()
    })

def show2(request):
    return render(request, 'show2.html',{
        'slideshow_items': Show.objects.all()
    })

def show3(request):
    return render(request, 'show3.html',{
        'slideshow_items': Show.objects.all()
    })

def show4(request):
    return render(request, 'show4.html',{
        'slideshow_items': Show.objects.all()
    })

def show5(request):
    return render(request, 'show5.html',{
        'slideshow_items': Show.objects.all()
    })