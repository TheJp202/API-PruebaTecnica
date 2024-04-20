from django.shortcuts import render
from rest_framework import generics
from .models import Bloque
from .serializers import BloqueSerializer

class BloqueLC_APIView(generics.ListCreateAPIView):
    queryset = Bloque.objects.all()
    serializer_class = BloqueSerializer
    
class BloqueRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bloque.objects.all()
    serializer_class = BloqueSerializer