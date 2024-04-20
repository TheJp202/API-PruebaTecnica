from rest_framework import serializers
from .models import BloqueCurso

class BloqueCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model=BloqueCurso
        fields='__all__'
        
        
