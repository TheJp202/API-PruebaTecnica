from rest_framework import serializers
from .models import EstudianteNota

class EstudianteNotaSerializer(serializers.ModelSerializer):
    class Meta:
        model=EstudianteNota
        fields='__all__'
        
class EstudianteNotaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstudianteNota
        fields = ['id', 'Nota'] 

    def update(self, instance, validated_data):
        instance.Nota = validated_data.get('Nota', instance.Nota)
        instance.save()
        return instance        
