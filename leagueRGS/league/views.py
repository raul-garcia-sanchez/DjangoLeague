from django.shortcuts import render, get_object_or_404

from .models import *

def clasificacion(request):
    equipos = Equipo.objects.all().order_by('-puntos')
    context = {'equipos': equipos}
    return render(request, 'league/clasificacion.html', context)

def pichichis(request):
    jugadores = Jugador.objects.all().order_by('-goles')[:10]
    context = {'jugadores':jugadores}
    return render(request, 'league/pichichis.html', context)

def seguimiento_partido(request, partido_id):
    partido = get_object_or_404(Partido, id=partido_id)
    eventos = Evento.objects.filter(partido=partido).order_by('tiempo')
    jugadores_local = Jugador.objects.filter(equipo=partido.local)
    jugadores_visitante = Jugador.objects.filter(equipo=partido.visitante)
    

    if request.method == 'POST':
        tipo = request.POST.get('tipo_evento')
        jugador_id = request.POST.get('jugador')
        tiempo = request.POST.get('tiempo')

        jugador = Jugador.objects.get(id=jugador_id)

        evento = Evento(tipo=tipo, jugador=jugador, partido=partido, tiempo=tiempo)
        evento.save()

        if tipo == 'Gol':
            if jugador.equipo == partido.local:
                partido.goles_local += 1
            else:
                partido.goles_visitante += 1
            partido.determinar_ganador()
            partido.save()

    return render(request, 'league/seguimiento_partido.html', {'partido': partido, 'eventos': eventos, 'jugadores_local': jugadores_local, 'jugadores_visitante': jugadores_visitante})

