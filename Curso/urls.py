from django.urls import path
from .views import CursoLC_APIView,CursoRUD_APIView

urlpatterns = [
    path('list_create/',CursoLC_APIView.as_view(),name='crear_listar_curso'),
    path('update_delete/<int:pk>',CursoRUD_APIView.as_view(),name='eliminar_actualizar_curso')
]