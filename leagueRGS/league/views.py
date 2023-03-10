from django.shortcuts import render

# Create your views here.
from .models import *

def clasificacion(request):
    equipos = Equipo.objects.all().order_by('-puntos', '-diferencia_goles')
    #Ordenar los equipos por puntos (descendente) y, en caso de empate, por diferencia de goles (descendente)
    context = {'equipos': equipos}
    return render(request, 'league/clasificacion.html', context)

