from rest_framework import generics
from .models import EstudianteBloque
from .serializers import EstudianteBloqueSerializer

class EstudianteBloqueLC_APIView(generics.ListCreateAPIView):
    queryset = EstudianteBloque.objects.all()
    serializer_class = EstudianteBloqueSerializer
    
class EstudianteBloqueRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EstudianteBloque.objects.all()
    serializer_class = EstudianteBloqueSerializer