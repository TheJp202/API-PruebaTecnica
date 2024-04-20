from rest_framework import generics
from .models import Estudiante
from .serializers import EstudianteSerializer

class EstudianteLC_APIView(generics.ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    
class EstudianteRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer