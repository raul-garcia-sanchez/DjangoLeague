from django.db import models

# Create your models here.

from django.db import models


class Liga(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)
    puntos = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    dorsal = models.PositiveIntegerField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.dorsal})"


class Partido(models.Model):
    local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='local')
    visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='visitante')
    fecha = models.DateField()
    hora = models.TimeField()
    goles_local = models.IntegerField(default=0)
    goles_visitante = models.IntegerField(default=0)
    ganador = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='ganador', null=True, blank=True)

    def __str__(self):
        return f'{self.local} vs {self.visitante}'

    def determinar_ganador(self):
        if self.goles_local > self.goles_visitante:
            self.ganador = self.local
        elif self.goles_local < self.goles_visitante:
            self.ganador = self.visitante
        else:
            self.ganador = None
        self.actualizar_clasificacion()

    def actualizar_clasificacion(self):
        # Actualizar la tabla de clasificación
        if self.ganador:
            # Sumar 3 puntos al equipo ganador
            self.ganador.puntos += 3
            self.ganador.goles_a_favor += self.goles_local if self.ganador == self.local else self.goles_visitante
            self.ganador.goles_en_contra += self.goles_visitante if self.ganador == self.local else self.goles_local
            self.ganador.save()

            # Actualizar los goles a favor y en contra del equipo perdedor
            perdedor = self.visitante if self.ganador == self.local else self.local
            perdedor.goles_a_favor += self.goles_visitante if self.ganador == self.local else self.goles_local
            perdedor.goles_en_contra += self.goles_local if self.ganador == self.local else self.goles_visitante
            perdedor.save()
        else:
            # Ambos equipos empataron, sumar 1 punto a cada uno
            self.local.puntos += 1
            self.visitante.puntos += 1
            self.local.save()
            self.visitante.save()

    
class Evento(models.Model):
    tipo = models.CharField(max_length=50)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    tiempo = models.PositiveIntegerField()  # en minutos

    def __str__(self):
        return f"{self.jugador} ({self.partido}): {self.tipo}"

