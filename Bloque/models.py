from django.db import models

class Bloque(models.Model):
    Nombre = models.CharField(max_length=10,unique=True)
    FechaInicio = models.DateField()
    FechaFinal = models.DateField()
    CostoFinal = models.IntegerField()
    def __str__(self):
        return self.Nombre