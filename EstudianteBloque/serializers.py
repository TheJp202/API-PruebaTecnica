from rest_framework import serializers
from .models import EstudianteBloque

class EstudianteBloqueSerializer(serializers.ModelSerializer):
    class Meta:
        model=EstudianteBloque
        fields='__all__'
        
        
