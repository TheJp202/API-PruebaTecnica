from django.urls import path
from .views import BloqueCuotaLC_APIView,BloqueCuotaRUD_APIView

urlpatterns = [
    path('list_create/',BloqueCuotaLC_APIView.as_view(),name='crear_listar_bloque_cuota'),
    path('update_delete/<int:pk>',BloqueCuotaRUD_APIView.as_view(),name='eliminar_actualizar_bloque_cuota')
]