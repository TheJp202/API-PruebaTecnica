from django.urls import path
from .views import BloqueCursoProfesorLC_APIView,BloqueCursoProfesorRUD_APIView

urlpatterns = [
    path('list_create/',BloqueCursoProfesorLC_APIView.as_view(),name='crear_listar_bloque_curso_profesor'),
    path('update_delete/<int:pk>',BloqueCursoProfesorRUD_APIView.as_view(),name='eliminar_actualizar_bloque_curso_profesor')
]