from rest_framework import generics
from .models import Elemento
from .serializers import ElementoSerializer

class ElementoLC_APIView(generics.ListCreateAPIView):
    queryset = Elemento.objects.all()
    serializer_class = ElementoSerializer
    
class ElementoRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Elemento.objects.all()
    serializer_class = ElementoSerializer