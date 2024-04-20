from django.urls import path
from .views import EstudianteLC_APIView,EstudianteRUD_APIView

urlpatterns = [
    path('list_create/',EstudianteLC_APIView.as_view(),name='crear_listar_estudiante'),
    path('update_delete/<int:pk>',EstudianteRUD_APIView.as_view(),name='eliminar_actualizar_estudiante')
]