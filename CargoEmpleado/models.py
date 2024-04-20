from django.db import models
from Cargo.models import Cargo
from Empleado.models import Empleado

class CargoEmpleado(models.Model):
    IdCargo = models.ForeignKey(Cargo, on_delete=models.CASCADE,to_field='id',db_column='IdCargo')
    IdEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE,to_field='id',db_column='IdEmpleado')
    def __str__(self):
        return f"Empleado:{self.IdEmpleado}, Cargo:{self.IdCargo}"
