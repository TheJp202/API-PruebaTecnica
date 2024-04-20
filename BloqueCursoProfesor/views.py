from rest_framework import generics
from .models import BloqueCursoProfesor
from .serializers import BloqueCursoProfesorSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class BloqueCursoProfesorLC_APIView(generics.ListCreateAPIView):
    queryset = BloqueCursoProfesor.objects.all()
    serializer_class = BloqueCursoProfesorSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]
    
class BloqueCursoProfesorRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BloqueCursoProfesor.objects.all()
    serializer_class = BloqueCursoProfesorSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]