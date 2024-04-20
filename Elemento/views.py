from rest_framework import generics
from .models import Elemento
from .serializers import ElementoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ElementoLC_APIView(generics.ListCreateAPIView):
    queryset = Elemento.objects.all()
    serializer_class = ElementoSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated] 
    
class ElementoRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Elemento.objects.all()
    serializer_class = ElementoSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated] 