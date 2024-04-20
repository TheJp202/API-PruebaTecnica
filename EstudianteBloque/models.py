from django.db import models
from Estudiante.models import Estudiante
from Bloque.models import Bloque

class EstudianteBloque(models.Model):
    IdEstudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE,to_field='id',db_column='IdEstudiante')
    IdBloque = models.ForeignKey(Bloque, on_delete=models.CASCADE,to_field='id',db_column='IdBloque')
    def __str__(self):
        return f"Estudiente:{self.IdEstudiante}, Bloque:{self.IdBloque}"