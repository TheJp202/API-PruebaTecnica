from rest_framework import generics
from .models import Cargo
from .serializers import CargoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CargoLC_APIView(generics.ListCreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]
     
class CargoRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated] 