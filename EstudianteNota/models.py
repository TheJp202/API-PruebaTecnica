from django.db import models
from EstudianteBloque.models import EstudianteBloque
from CursoElemento.models import CursoElemento

class EstudianteNota(models.Model):
    IdEstudianteBloque = models.ForeignKey(EstudianteBloque, on_delete=models.CASCADE,to_field='id',db_column='IdEstudianteBloque')
    IdCursoElemento = models.ForeignKey(CursoElemento, on_delete=models.CASCADE,to_field='id',db_column='IdCursoElemento')    
    Nota = models.DecimalField(max_digits=3,decimal_places=1)
    def __str__(self):
        return f"EstudianteBloque: {self.IdEstudianteBloque}, CursoElemento: {self.IdCursoElemento}, Nota: {self.Nota}"
