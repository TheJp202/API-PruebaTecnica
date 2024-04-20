from rest_framework import generics
from .models import BloqueCurso
from .serializers import BloqueCursoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class BloqueCursoLC_APIView(generics.ListCreateAPIView):
    queryset = BloqueCurso.objects.all()
    serializer_class = BloqueCursoSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]
    
class BloqueCursoRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BloqueCurso.objects.all()
    serializer_class = BloqueCursoSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]