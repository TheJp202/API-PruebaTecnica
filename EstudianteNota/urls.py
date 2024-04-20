from django.urls import path
from .views import EstudianteNotaLC_APIView,EstudianteNotaRUD_APIView

urlpatterns = [
    path('list_create/',EstudianteNotaLC_APIView.as_view(),name='crear_listar_estudiante_nota'),
    path('update_delete/<int:pk>',EstudianteNotaRUD_APIView.as_view(),name='eliminar_actualizar_estudiante_nota')
]