from django.db import models
from BloqueCurso.models import BloqueCurso
from Empleado.models import Empleado

class BloqueCursoProfesor(models.Model):
    IdBloqueCurso = models.ForeignKey(BloqueCurso, on_delete=models.CASCADE,to_field='id',db_column='IdBloqueCurso')
    IdProfesor = models.ForeignKey(Empleado, on_delete=models.CASCADE,to_field='id',db_column='IdProfesor')
    def __str__(self):
        return f"BloqueCurso:{self.IdBloqueCurso}, Profesor:{self.IdProfesor}"