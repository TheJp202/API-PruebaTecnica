from django.db import models

class Elemento(models.Model):
    Nombre = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.Nombre