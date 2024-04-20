from rest_framework import serializers
from .models import CursoElemento

class CursoElementoSerializer(serializers.ModelSerializer):
    class Meta:
        model=CursoElemento
        fields='__all__'
        
        