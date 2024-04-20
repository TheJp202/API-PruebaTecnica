from rest_framework import generics
from .models import EstudianteNota
from .serializers import EstudianteNotaSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class EstudianteNotaLC_APIView(generics.ListCreateAPIView):
    queryset = EstudianteNota.objects.all()
    serializer_class = EstudianteNotaSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]
    
class EstudianteNotaRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EstudianteNota.objects.all()
    serializer_class = EstudianteNotaSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]