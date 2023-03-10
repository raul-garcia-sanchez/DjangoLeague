from django.contrib import admin

# Register your models here.

from .models import *

class LigaAdmin(admin.ModelAdmin):
    list_display = ['nombre']

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'liga', 'puntos')

class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dorsal', 'equipo')

class PartidoAdmin(admin.ModelAdmin):
    list_display = ('local','visitante','fecha','hora','goles_local','goles_visitante','ganador')

class EventoAdmin(admin.ModelAdmin):
    list_display = ('tipo','jugador','partido','tiempo')

admin.site.register(Liga,LigaAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Partido, PartidoAdmin)
admin.site.register(Evento, EventoAdmin)