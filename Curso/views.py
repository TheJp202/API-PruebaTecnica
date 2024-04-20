from rest_framework import generics
from .models import Curso
from .serializers import CursoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CursoLC_APIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]
    
class CursoRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]