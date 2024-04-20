from django.urls import path
from .views import BloqueCursoLC_APIView,BloqueCursoRUD_APIView

urlpatterns = [
    path('list_create/',BloqueCursoLC_APIView.as_view(),name='crear_listar_bloque_curso'),
    path('update_delete/<int:pk>',BloqueCursoRUD_APIView.as_view(),name='eliminar_actualizar_bloque_curso')
]