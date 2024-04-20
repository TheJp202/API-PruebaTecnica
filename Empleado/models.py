from django.db import models

class Empleado(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    DNI = models.CharField(max_length=8,unique=True)
    Telefono = models.CharField(max_length=9)
    Correo = models.CharField(max_length=50)
    Contraseña = models.CharField()
    FechaContratacion = models.DateField()
    def __str__(self):
        return self.DNI
        
    
    