from rest_framework import generics
from .models import CursoElemento
from .serializers import CursoElementoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CursoElementoLC_APIView(generics.ListCreateAPIView):
    queryset = CursoElemento.objects.all()
    serializer_class = CursoElementoSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]
    
class CursoElementoRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CursoElemento.objects.all()
    serializer_class = CursoElementoSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]