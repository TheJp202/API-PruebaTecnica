from rest_framework import serializers
from .models import CargoEmpleado

class CargoEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=CargoEmpleado
        fields='__all__'
        
        
