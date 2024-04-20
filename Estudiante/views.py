from rest_framework import generics
from .models import Estudiante
from .serializers import EstudianteSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class EstudianteLC_APIView(generics.ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]

    
class EstudianteRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]