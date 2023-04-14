from django.contrib import admin
from .models import *

# Register your models here.
class JugadorAdmin(admin.ModelAdmin):
    list_display = [
        'alias',
        'nom_jugador',
        'cognnoms_jugador',
        'dorsal',
        'gols',
        'asistencies',
        'targeta_vermella',
        'targeta_groga'
    ]
    
class EquipAdmin(admin.ModelAdmin):
    list_display = [
        'nom_equip'
    ]

class LligaAdmin(admin.ModelAdmin):
    list_display = [
        'nom_lliga'
    ]



class EventInline(admin.TabularInline):
    model = Event
    fields = ["tipus","equip","temps","jugador","jugador2","detalls"]
    ordering = ("temps",)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # filtrem els jugadors i només deixem els que siguin d'algun dels 2 equips (local o visitant)
        if db_field.name == "jugador":
            partit_id = request.resolver_match.kwargs['object_id']
            partit = Partit.objects.get(id=partit_id)
            jugadors_local = [jugador.id for jugador in partit.equip_local.jugador.all()]
            jugadors_visitant = [jugador.id for jugador in partit.equip_visitant.jugador.all()]
            jugadors = jugadors_local + jugadors_visitant
            kwargs["queryset"] = Jugador.objects.filter(id__in=jugadors)    
        if db_field.name == "jugador2":
            partit_id = request.resolver_match.kwargs['object_id']
            partit = Partit.objects.get(id=partit_id)
            jugadors_local = [jugador.id for jugador in partit.equip_local.jugador.all()]
            jugadors_visitant = [jugador.id for jugador in partit.equip_visitant.jugador.all()]
            jugadors = jugadors_local + jugadors_visitant
            kwargs["queryset"] = Jugador.objects.filter(id__in=jugadors)

        if db_field.name == "equip":
            partit_id = request.resolver_match.kwargs['object_id']
            partit = Partit.objects.get(id=partit_id)
            local = [partit.equip_local.id]
            visitant = [partit.equip_visitant.id]
            equips = local + visitant
            kwargs["queryset"] = Equip.objects.filter(id__in=equips)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class partitAdmin(admin.ModelAdmin):
    search_fields = ["equip_local","equip_visitant","resultat", "lliga"]
    readonly_fields = ["data_partit","lliga","equip_local","equip_visitant","resultat",]
    list_display = ["equip_local", "equip_visitant", "resultat","lliga","data_partit"]
    inlines = [EventInline,]
    def resultat(self,obj):
        gols_local = obj.event_set.filter(tipus = Event.EventType.GOL,equip = obj.equip_local).count()
        gols_visitant = obj.event_set.filter(tipus = Event.EventType.GOL,equip = obj.equip_visitant).count()
        return "{} - {}".format(gols_local,gols_visitant)

admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Equip, EquipAdmin)
admin.site.register(Lliga, LligaAdmin)
admin.site.register(Partit, partitAdmin)