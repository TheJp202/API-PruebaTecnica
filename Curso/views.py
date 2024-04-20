from rest_framework import generics
from .models import Curso
from .serializers import CursoSerializer

class CursoLC_APIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class CursoRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer