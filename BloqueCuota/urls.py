from django.urls import path
from .views import BloqueCuotaLC_APIView,BloqueCuotaRUD_APIView,ObtenerIdEstudianteCuota_APIView,BloqueCuotaUpdateAPIView

urlpatterns = [
    path('list_create/',BloqueCuotaLC_APIView.as_view(),name='crear_listar_bloque_cuota'),
    path('update_delete/<int:pk>',BloqueCuotaRUD_APIView.as_view(),name='eliminar_actualizar_bloque_cuota'),
    path('get_id_cuota/<str:num_cuota>/<str:id_estudiante>',ObtenerIdEstudianteCuota_APIView.as_view(),name='obtener_id_cuota'),
    path('only_update/<int:pk>',BloqueCuotaUpdateAPIView.as_view(),name='actualizar_cuota')
]