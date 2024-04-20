from rest_framework import generics
from .models import CursoElemento
from .serializers import CursoElementoSerializer

class CursoElementoLC_APIView(generics.ListCreateAPIView):
    queryset = CursoElemento.objects.all()
    serializer_class = CursoElementoSerializer
    
class CursoElementoRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CursoElemento.objects.all()
    serializer_class = CursoElementoSerializer