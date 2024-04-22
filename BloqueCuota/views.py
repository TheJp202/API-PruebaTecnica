from rest_framework import generics
from .models import BloqueCuota
from .serializers import BloqueCuotaSerializer,BloqueCuotaUpdateSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection


class BloqueCuotaLC_APIView(generics.ListCreateAPIView):
    queryset = BloqueCuota.objects.all()
    serializer_class = BloqueCuotaSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]
    
class BloqueCuotaRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BloqueCuota.objects.all()
    serializer_class = BloqueCuotaSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]
    
class BloqueCuotaUpdateAPIView(generics.UpdateAPIView):
    queryset=BloqueCuota.objects.all()
    serializer_class=BloqueCuotaUpdateSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]        
    
class ObtenerIdEstudianteCuota_APIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,num_cuota,id_estudiante, format=None):
        query = """
            SELECT * FROM obtener_id_estudiante_cuota(%s,%s)
        """
        with connection.cursor() as cursor:
            cursor.execute(query,[num_cuota,id_estudiante])
            resultados = dictfetchall(cursor)
        return Response(resultados)
    
    

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]