from django.shortcuts import render
from app.models import Show


def home(request):
    return render(request, 'home.html', {'shows': Show.objects.all()})

def directions(request):
    return render(request, 'directions.html')

def merchandise(request):
    return render(request, 'merchandise.html')

def tickets(request):
    return render(request, 'tickets.html')

def shows(request):
    return render(request, 'shows.html', {'shows': Show.objects.all()})