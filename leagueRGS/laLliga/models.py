from django.db import models

# Create your models here.

class Jugador(models.Model):
    alias = models.CharField(max_length=200)
    nom_jugador = models.CharField(max_length=50)
    cognnoms_jugador = models.CharField(max_length=50)
    dorsal = models.IntegerField(null=True)
    gols = models.IntegerField(null=True)
    asistencies = models.IntegerField(null=True)
    targeta_vermella = models.IntegerField(null=True)
    targeta_groga = models.IntegerField(null=True)
    def __str__ (self):
        equip_actual = self.equip_set.first()
        return "{} ({})".format(self.alias,equip_actual)
class Equip(models.Model):
    nom_equip = models.CharField(max_length=50)
    jugador = models.ManyToManyField(Jugador)
    def __str__ (self):
        return self.nom_equip

class Lliga(models.Model):
    nom_lliga = models.CharField(max_length=50)
    equips = models.ManyToManyField(Equip)
    temporada = models.IntegerField(null=True)
    def __str__ (self):
        return self.nom_lliga


class Partit(models.Model):
    equip_local = models.ForeignKey(Equip, on_delete=models.CASCADE, related_name='local') 
    equip_visitant = models.ForeignKey(Equip, on_delete=models.CASCADE, related_name='visitant')
    data_partit = models.DateField(null=True)
    lliga = models.ForeignKey(Lliga, on_delete=models.CASCADE)
    def __str__ (self):
        local = self.equip_local
        visitant = self.equip_visitant
        return  "{} - {}".format(local,visitant)
    def gols_local(self):
            return self.event_set.filter(tipus=Event.EventType.GOL,equip=self.equip_local).count()
    def gols_visitant(self):
        return self.event_set.filter(tipus=Event.EventType.GOL,equip=self.equip_visitant).count()
class Event(models.Model):
    class EventType(models.TextChoices):
        GOL = "GOL"
        AUTOGOL = "AUTOGOL"
        FALTA = "FALTA"
        PENALTY = "PENALTI"
        MANS = "MANS"
        CESSIO = "CESSIO"
        FORA_DE_JOC = "FORA_DE_JOC"
        ASSISTENCIA = "ASSISTENCIA"
        TARGETA_GROGA = "TARGETA_GROGA"
        TARGETA_VERMELLA = "TARGETA_VERMELLA"

    temps = models.TimeField()
    partit = models.ForeignKey(Partit, on_delete=models.CASCADE)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE,
                    related_name="jugador")
    equip = models.ForeignKey(Equip, on_delete=models.CASCADE)
    tipus = models.CharField(max_length=50, choices=EventType.choices)
    jugador2 = models.ForeignKey(Jugador,null=True,blank=True,
                    on_delete=models.SET_NULL,
                    related_name="events_rebuts")
    detalls = models.TextField(null=True,blank=True)    
    def __str__ (self):
        return self.tipus
