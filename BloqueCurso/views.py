from rest_framework import generics
from .models import BloqueCurso
from .serializers import BloqueCursoSerializer

class BloqueCursoLC_APIView(generics.ListCreateAPIView):
    queryset = BloqueCurso.objects.all()
    serializer_class = BloqueCursoSerializer
    
class BloqueCursoRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BloqueCurso.objects.all()
    serializer_class = BloqueCursoSerializer