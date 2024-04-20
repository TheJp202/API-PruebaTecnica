from django.db import models
from EstudianteBloque.models import EstudianteBloque

class BloqueCuota(models.Model):
    IdEstudianteBloque = models.ForeignKey(EstudianteBloque, on_delete=models.CASCADE,to_field='id',db_column='IdEstudianteBloque')
    NumeroCuota = models.CharField(max_length=2)
    Monto = models.DecimalField(max_digits=6,decimal_places=2)
    Estado = models.BooleanField(default=False)
    def __str__(self):
        return f"EstudianteBloque: {self.IdEstudianteBloque}, NumeroCuota: {self.NumeroCuota}, Estado: {self.Estado}"
