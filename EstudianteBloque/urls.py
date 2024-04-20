from django.urls import path
from .views import EstudianteBloqueLC_APIView,EstudianteBloqueRUD_APIView

urlpatterns = [
    path('list_create/',EstudianteBloqueLC_APIView.as_view(),name='crear_listar_estudiante_bloque'),
    path('update_delete/<int:pk>',EstudianteBloqueRUD_APIView.as_view(),name='eliminar_actualizar_estudiante_bloque')
]