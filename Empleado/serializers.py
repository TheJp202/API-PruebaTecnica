from rest_framework import serializers
from .models import Empleado
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empleado
        fields='__all__'