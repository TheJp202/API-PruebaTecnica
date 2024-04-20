from django.urls import path
from .views import BloqueLC_APIView,BloqueRUD_APIView

urlpatterns = [
    path('list_create/',BloqueLC_APIView.as_view(),name='crear_listar_bloque'),
    path('update_delete/<int:pk>',BloqueRUD_APIView.as_view(),name='eliminar_actualizar_bloque')
]