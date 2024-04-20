from django.urls import path
from .views import CursoElementoLC_APIView,CursoElementoRUD_APIView

urlpatterns = [
    path('list_create/',CursoElementoLC_APIView.as_view(),name='crear_listar_curso_elemento'),
    path('update_delete/<int:pk>',CursoElementoRUD_APIView.as_view(),name='eliminar_actualizar_curso_elemento')
]