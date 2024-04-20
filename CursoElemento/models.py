from django.db import models
from django.db import models
from Curso.models import Curso
from Elemento.models import Elemento

class CursoElemento(models.Model):
    IdCurso = models.ForeignKey(Curso, on_delete=models.CASCADE,to_field='id',db_column='IdCurso')
    IdElemento = models.ForeignKey(Elemento, on_delete=models.CASCADE,to_field='id',db_column='IdElemento')
    def __str__(self):
        return f"Curso:{self.IdCurso}, Elemento:{self.IdElemento}"