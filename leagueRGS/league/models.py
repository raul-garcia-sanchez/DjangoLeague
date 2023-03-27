from django.db import models


from django.db import models


class Liga(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    dorsal = models.PositiveIntegerField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    goles = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nombre', 'dorsal', 'equipo'], name='pk_jugador')
        ]

    def __str__(self):
        return f"{self.nombre} ({self.dorsal})"



class Partido(models.Model):
    local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='local')
    visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='visitante')
    fecha = models.DateField()
    hora = models.TimeField()
    goles_local = models.IntegerField(default=0)
    goles_visitante = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['local', 'visitante'], name='unique_match'),
        ]

    def __str__(self):
        return f'{self.local} vs {self.visitante}'
    
    def get_goles_local(self):
        return self.goles_local

    def get_goles_visitante(self):
        return self.goles_visitante

class TipoEvento(models.Model):
    tipo = models.CharField(max_length = 50)

    def __str__(self):
        return self.tipo
    
class Evento(models.Model):
    tipo = models.ForeignKey(TipoEvento, on_delete=models.CASCADE)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, related_name='eventos')
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='eventos', null=True, blank=True)
    tiempo = models.PositiveIntegerField()

    # def save(self, *args, **kwargs):
    #     self.equipo = self.jugador.equipo
    #     #super(Evento, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(Evento, self).save(*args, **kwargs)
        if str(self.tipo) == 'Gol':
            print("entro")
            if self.equipo == self.partido.local:
                self.partido.goles_local += 1
                self.partido.save()
            elif self.equipo == self.partido.visitante:
                self.partido.goles_visitante += 1
                self.partido.save()

    def __str__(self):
        return f"{self.jugador} ({self.partido}): {self.tipo}"
