from django.db import models
from django.contrib.auth.models import User

class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    DNI = models.CharField(max_length=8,unique=True)
    Telefono = models.CharField(max_length=9)
    Correo = models.CharField(max_length=50)
    Contraseña = models.CharField()
    FechaContratacion = models.DateField()
    def __str__(self):
        return self.DNI
    
    def save(self, *args, **kwargs):
        if not self.user_id:
            user = User.objects.create(username=self.DNI, email=self.Correo)
            user.set_password(self.Contraseña)
            user.save()
            self.user = user
        super().save(*args, **kwargs)
    
    
    
    