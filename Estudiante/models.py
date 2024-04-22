from django.db import models

class Estudiante(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    DNI = models.CharField(max_length=8,unique=True)
    Telefono = models.CharField(max_length=9)
    Correo = models.CharField(max_length=50)
    Contraseña = models.CharField()
    FechaAdmision = models.DateField(auto_now_add=True)
    Semestre = models.CharField(max_length=2,blank=True)
    def __str__(self):
        return self.DNI
        