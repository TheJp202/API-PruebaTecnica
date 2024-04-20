from rest_framework import generics
from .models import BloqueCuota
from .serializers import BloqueCuotaSerializer

class BloqueCuotaLC_APIView(generics.ListCreateAPIView):
    queryset = BloqueCuota.objects.all()
    serializer_class = BloqueCuotaSerializer
    
class BloqueCuotaRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BloqueCuota.objects.all()
    serializer_class = BloqueCuotaSerializer