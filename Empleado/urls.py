from django.urls import path
from .views import EmpleadoLC_APIView,EmpleadoRUD_APIView

urlpatterns = [
    path('list_create/',EmpleadoLC_APIView.as_view(),name='crear_listar_empleado'),
    path('update_delete/<int:pk>',EmpleadoRUD_APIView.as_view(),name='eliminar_actualizar_empleado')
]