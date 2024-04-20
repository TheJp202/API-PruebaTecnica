from rest_framework import generics
from .models import EstudianteBloque
from .serializers import EstudianteBloqueSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class EstudianteBloqueLC_APIView(generics.ListCreateAPIView):
    queryset = EstudianteBloque.objects.all()
    serializer_class = EstudianteBloqueSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]
    
class EstudianteBloqueRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EstudianteBloque.objects.all()
    serializer_class = EstudianteBloqueSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]