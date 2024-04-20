from rest_framework import generics
from .models import CargoEmpleado
from .serializers import CargoEmpleadoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CargoEmpleadoLC_APIView(generics.ListCreateAPIView):
    queryset = CargoEmpleado.objects.all()
    serializer_class = CargoEmpleadoSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]
    
class CargoEmpleadoRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CargoEmpleado.objects.all()
    serializer_class = CargoEmpleadoSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]
    