from rest_framework import generics
from .models import BloqueCursoProfesor
from .serializers import BloqueCursoProfesorSerializer

class BloqueCursoProfesorLC_APIView(generics.ListCreateAPIView):
    queryset = BloqueCursoProfesor.objects.all()
    serializer_class = BloqueCursoProfesorSerializer
    
class BloqueCursoProfesorRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BloqueCursoProfesor.objects.all()
    serializer_class = BloqueCursoProfesorSerializer