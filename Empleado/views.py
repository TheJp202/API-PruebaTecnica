from rest_framework import generics,status
from .models import Empleado
from .serializers import EmpleadoSerializer  
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from django.db import connection

class EmpleadoL_APIView(generics.ListAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]


class RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = EmpleadoSerializer(data=request.data)
        if serializer.is_valid():
            empleado = serializer.save()
            token, created = Token.objects.get_or_create(user=empleado.user)
            return Response({'token': token.key, "empleado": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        dni = request.data.get('DNI') 
        password = request.data.get('Contraseña')
        empleado = get_object_or_404(Empleado, DNI=dni)
        if not empleado.user.check_password(password):
            return Response({"error": "Contraseña invalida"}, status=status.HTTP_400_BAD_REQUEST)
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM obtener_datos_empleado(%s)", [empleado.id])
            datos_empleado = dictfetchall(cursor)
        if datos_empleado:
            empleado_data = datos_empleado[0] 
        else:
            empleado_data = {}
        token, created = Token.objects.get_or_create(user=empleado.user)
        response_data = {
            "token": token.key,
            "empleado": empleado_data
        }
        return Response(response_data, status=status.HTTP_200_OK)
    


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]