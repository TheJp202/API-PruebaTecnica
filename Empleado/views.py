from rest_framework import generics
from .models import Empleado
from .serializers import EmpleadoSerializer

class EmpleadoLC_APIView(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    
class EmpleadoRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer