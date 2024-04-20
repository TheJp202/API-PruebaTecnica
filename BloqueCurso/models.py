from django.db import models
from Bloque.models import Bloque
from Curso.models import Curso

class BloqueCurso(models.Model):
    IdBloque = models.ForeignKey(Bloque, on_delete=models.CASCADE,to_field='id',db_column='IdBloque')
    IdCurso = models.ForeignKey(Curso, on_delete=models.CASCADE,to_field='id',db_column='IdCurso')
    def __str__(self):
        return f"Bloque:{self.IdBloque}, Curso:{self.IdCurso}"