from rest_framework import serializers
from .models import BloqueCuota

class BloqueCuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model=BloqueCuota
        fields='__all__'
        
        
