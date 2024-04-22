from rest_framework import generics
from .models import EstudianteNota
from .serializers import EstudianteNotaSerializer,EstudianteNotaUpdateSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection


class EstudianteNotaLC_APIView(generics.ListCreateAPIView):
    queryset = EstudianteNota.objects.all()
    serializer_class = EstudianteNotaSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]
    
class EstudianteNotaRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EstudianteNota.objects.all()
    serializer_class = EstudianteNotaSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]
    
    
class EstudianteNotaUpdateAPIView(generics.UpdateAPIView):
    queryset=EstudianteNota.objects.all()
    serializer_class=EstudianteNotaUpdateSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]    
    
class ObtenerIdEvaluacionAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, dni,curso,elemento, format=None):
        query = """
                SELECT * FROM obteneridevaluacion(%s,%s,%s)        
                """
        with connection.cursor() as cursor:
            cursor.execute(query, [dni,curso,elemento])
            resultados = dictfetchall(cursor)
        return Response(resultados)


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]