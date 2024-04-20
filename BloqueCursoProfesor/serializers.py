from rest_framework import serializers
from .models import BloqueCursoProfesor

class BloqueCursoProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model=BloqueCursoProfesor
        fields='__all__'
        
        
