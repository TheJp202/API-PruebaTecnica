from rest_framework import generics
from .models import EstudianteNota
from .serializers import EstudianteNotaSerializer

class EstudianteNotaLC_APIView(generics.ListCreateAPIView):
    queryset = EstudianteNota.objects.all()
    serializer_class = EstudianteNotaSerializer
    
class EstudianteNotaRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EstudianteNota.objects.all()
    serializer_class = EstudianteNotaSerializer