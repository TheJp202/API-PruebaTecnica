from rest_framework import generics
from .models import Estudiante
from .serializers import EstudianteAllSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection

class EstudianteLC_APIView(generics.ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteAllSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]

    
class EstudianteRUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteAllSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]
    
    
    
class ObtenerResultadoProfesorAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, id_profesor, format=None):
        query = """
            SELECT * FROM obtener_resultado_estudiantes_pro(%s)
        """
        with connection.cursor() as cursor:
            cursor.execute(query, [id_profesor])
            resultados = dictfetchall(cursor)
        return Response(resultados)

class ObtenerResultadoAdminAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query = """
            SELECT * FROM obtener_resultado_estudiantes_admin()
        """
        with connection.cursor() as cursor:
            cursor.execute(query)
            resultados = dictfetchall(cursor)
        return Response(resultados)

class ObtenerResultadoAdminProAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query = """
            SELECT * FROM obtener_resultado_estudiantes_admin_pro()
        """
        with connection.cursor() as cursor:
            cursor.execute(query)
            resultados = dictfetchall(cursor)
        return Response(resultados)

class CrearEstudianteConBloqueAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,nombre,apellido,dni,telefono,correo,contraseña,bloque, format=None):
        query = """
            SELECT insertar_estudiante_y_bloque(%s,%s,%s,%s,%s,%s,%s)
        """
        with connection.cursor() as cursor:
            cursor.execute(query,[nombre,apellido,dni,telefono,correo,contraseña,bloque])
            resultados = dictfetchall(cursor)
        return Response(resultados)

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    
    
    
