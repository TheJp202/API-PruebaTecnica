from rest_framework import generics
from .models import Cargo
from .serializers import CargoSerializer

class CargoLC_APIView(generics.ListCreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    
class CargoRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer