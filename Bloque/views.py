from django.shortcuts import render
from rest_framework import generics
from .models import Bloque
from .serializers import BloqueSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class BloqueLC_APIView(generics.ListCreateAPIView):
    queryset = Bloque.objects.all()
    serializer_class = BloqueSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]
        
class BloqueRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bloque.objects.all()
    serializer_class = BloqueSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]