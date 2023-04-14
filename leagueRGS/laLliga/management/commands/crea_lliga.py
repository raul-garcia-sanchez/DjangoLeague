from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from faker import Faker
from datetime import timedelta
from random import randint
from django.utils import timezone
from laLliga.models import *

faker = Faker(["es_CA","es_ES"])

class Command(BaseCommand):
    help = 'Crea una lliga amb equips i jugadors'

    def add_arguments(self, parser):
        parser.add_argument('titol_lliga', nargs=1, type=str)

    def handle(self, *args, **options):
        titol_lliga = options['titol_lliga'][0]
        lliga = Lliga.objects.filter(nom_lliga=titol_lliga)
        if lliga.count()>0:
            print("Aquesta lliga ja està creada. Posa un altre nom.")
            return

        print("Creem la nova lliga: {}".format(titol_lliga))
        lliga = Lliga(nom_lliga=titol_lliga)
        lliga.save()

        print("Creem equips")
        prefixos = ["RCD", "Athletic", "", "Deportivo", "Unión Deportiva"]
        for i in range(20):
            ciutat = faker.city()
            prefix = prefixos[randint(0,len(prefixos)-1)]
            if prefix:
                prefix += " "
            nom =  prefix + ciutat
            equip = Equip(nom_equip=nom)
            #print(equip)
            equip.save()
            lliga.equips.add(equip)

            print("Creem jugadors de l'equip "+nom)
            for i in range(25):
                nom_jugador = faker.first_name()
                cognnoms_jugador = faker.last_name()
                jugador = Jugador(nom_jugador=nom_jugador,cognnoms_jugador=cognnoms_jugador,alias=nom_jugador+" "+cognnoms_jugador)
                #print(jugador)
                jugador.save()
                equip.jugador.add(jugador)

        print("Creem partits de la lliga")
        for local in lliga.equips.all():
            for visitant in lliga.equips.all():
                if local!=visitant:
                    partit = Partit()
                    partit.equip_local = local
                    partit.equip_visitant = visitant
                    partit.lliga = lliga

                    if Partit.objects.filter(equip_local=local,equip_visitant=visitant,lliga=lliga)

                    partit.save()

                    random_gols_Local= randint(0,5)
                    random_gols_Visitant = randint(0,5)
                    for i in range(random_gols_Local):
                        jugadores = local.jugador.all()
                        jugadorRandom = randint(0,len(jugadores)-1)
                        event = Event(tipus=Event.EventType.GOL,jugador =jugadores[jugadorRandom],equip=local,partit = partit,temps = timezone.now(),jugador2= jugadores[jugadorRandom])
                        event.save()

                    for i in range(random_gols_Visitant):
                        jugadores = visitant.jugador.all()
                        jugadorRandom = randint(0,len(jugadores)-1)
                        event = Event(tipus=Event.EventType.GOL,jugador =jugadores[jugadorRandom],equip=visitant,partit = partit,temps = timezone.now(),jugador2= jugadores[jugadorRandom])
                        event.save()