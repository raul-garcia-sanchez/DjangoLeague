from django.contrib import admin
from django.db.models import Q

# Register your models here.

from .models import *

class LigaAdmin(admin.ModelAdmin):
    list_display = ['nombre']

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'liga')

class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dorsal', 'equipo')

class EventInline(admin.TabularInline):
    model = Evento
    fields = ('tipo','jugador','partido','equipo','tiempo')
    ordering = ('tiempo',)  

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "jugador":
    #         match_id = request.resolver_match.kwargs['object_id']
    #         match = Partido.objects.get(pk=match_id)
    #         kwargs["queryset"] = Jugador.objects.filter(equipo__in=[match.local, match.visitante])
    #     elif db_field.name == "equipo":
    #         match_id = request.resolver_match.kwargs['object_id']
    #         match = Partido.objects.get(pk=match_id)
    #         kwargs["queryset"] = Equipo.objects.filter(Q(nombre=match.local) | Q(nombre=match.visitante ))
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
class PartidoAdmin(admin.ModelAdmin):
    list_display = ('local', 'visitante', 'fecha', 'hora', 'goles_local', 'goles_visitante')
    readonly_fields = ('local', 'visitante', 'fecha', 'hora', 'goles_local', 'goles_visitante', 'resultado')
    inlines = (EventInline,)
    def resultado(self, obj):
        return str(obj.goles_local) +  " - " + str(obj.goles_visitante)

class EventoAdmin(admin.ModelAdmin):
    list_display = ('tipo','jugador','partido','tiempo')

class TipoEventoAdmin(admin.ModelAdmin):
    list_display = ['tipo']

admin.site.register(Liga,LigaAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Partido, PartidoAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(TipoEvento, TipoEventoAdmin)