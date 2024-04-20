from django.db import models

class Curso(models.Model):
    Nombre = models.CharField(max_length=80,unique=True)
    DuracionHora = models.IntegerField()
    Costo = models.IntegerField()
    def __str__(self):
        return self.Nombre