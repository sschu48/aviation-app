from django.shortcuts import render
from django.http import HttpResponse

# Dummy Data
metars = [
    {
        'airport': 'Greeley Weld',
        'icao': 'KGXY',
        'wind': '220 12k'
    },
    {
        'airport': 'Fort Collins',
        'icao': 'KFNL',
        'wind': '270 5k'
    }
]

# Create your views here.
def home(request):
    return render(request, 'weather/home.html', {'title': 'Weather'})

def taf(request):
    return render(request, 'weather/taf.html', {'title': 'TAF'})

def metar(request):
    context = {
        'metars': metars
    }
    return render(request, 'weather/metar.html', {'title': 'METAR'})
