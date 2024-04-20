from rest_framework import serializers
from .models import EstudianteNota

class EstudianteNotaSerializer(serializers.ModelSerializer):
    class Meta:
        model=EstudianteNota
        fields='__all__'
        
        
