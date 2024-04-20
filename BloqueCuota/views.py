from rest_framework import generics
from .models import BloqueCuota
from .serializers import BloqueCuotaSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class BloqueCuotaLC_APIView(generics.ListCreateAPIView):
    queryset = BloqueCuota.objects.all()
    serializer_class = BloqueCuotaSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]
    
class BloqueCuotaRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BloqueCuota.objects.all()
    serializer_class = BloqueCuotaSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]