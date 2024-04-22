from rest_framework import serializers
from .models import BloqueCuota

class BloqueCuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model=BloqueCuota
        fields='__all__'
        
class BloqueCuotaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloqueCuota
        fields = ['id', 'Monto', 'Estado'] 

    def update(self, instance, validated_data):
        if 'Monto' in validated_data:
            instance.Monto = validated_data['Monto']
        if 'Estado' in validated_data:
            instance.Estado = validated_data['Estado']
        instance.save()
        return instance 
        
