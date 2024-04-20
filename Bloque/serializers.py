from rest_framework import serializers
from .models import Bloque

class BloqueSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bloque
        fields='__all__'
        
        
