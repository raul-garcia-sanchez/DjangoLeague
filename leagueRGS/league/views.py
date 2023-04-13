from django.shortcuts import render, get_object_or_404
from django import forms
from django.shortcuts import redirect

from .models import *
from league.models import *

def clasificacion(request, liga_id=None):
    lliga = Liga.objects.get(pk=liga_id)
    equips = lliga.equipo_set.all()
    classi = []

    for equip in equips:
        punts = 0
        gols_a_favor = 0
        gols_en_contra = 0

        partits_local = equip.local.all()
        partits_visitant = equip.visitante.all()

        for partit in partits_local:
            if partit.goles_local > partit.goles_visitante:
                punts += 3
            elif partit.goles_local == partit.goles_visitante:
                punts += 1
            gols_a_favor += partit.goles_local
            gols_en_contra += partit.goles_visitante

        for partit in partits_visitant:
            if partit.goles_visitante > partit.goles_local:
                punts += 3
            elif partit.goles_visitante == partit.goles_local:
                punts += 1
            gols_a_favor += partit.goles_visitante
            gols_en_contra += partit.goles_local

        classi.append({
            'equip': equip.nombre,
            'punts': punts,
            'gols_a_favor': gols_a_favor,
            'gols_en_contra': gols_en_contra,
            'diferencia_gols': gols_a_favor - gols_en_contra
        })

    classi = sorted(classi, key=lambda e: (-e['punts'], -e['diferencia_gols']))

    return render(request, 'league/clasificacion.html', {'classi': classi})

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

class MenuForm(forms.Form):
    lliga = forms.ModelChoiceField(queryset=Liga.objects.all())

def menu(request):
    form = MenuForm()
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            liga = form.cleaned_data.get("lliga")
            return redirect('/liga/clasificacion/'+str(liga.id))
    return render(request, "league/menu.html",{
                    "form": form,
            })