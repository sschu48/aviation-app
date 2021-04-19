from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return(HttpResponse('<h1>Weather Home</h1>'))

def taf(request):
    return(HttpResponse('<h1>Weather TAFs</h1>'))

def metar(request):
    return(HttpResponse('<h1>Weather METARs</h1>'))
