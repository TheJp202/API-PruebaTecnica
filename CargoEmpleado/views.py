from rest_framework import generics
from .models import CargoEmpleado
from .serializers import CargoEmpleadoSerializer

class CargoEmpleadoLC_APIView(generics.ListCreateAPIView):
    queryset = CargoEmpleado.objects.all()
    serializer_class = CargoEmpleadoSerializer
    
class CargoEmpleadoRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CargoEmpleado.objects.all()
    serializer_class = CargoEmpleadoSerializer