from django.urls import path
from .views import CargoEmpleadoLC_APIView,CargoEmpleadoRUD_APIView

urlpatterns = [
    path('list_create/',CargoEmpleadoLC_APIView.as_view(),name='crear_listar_cargo_empleado'),
    path('update_delete/<int:pk>',CargoEmpleadoRUD_APIView.as_view(),name='eliminar_actualizar_cargo_empleado')
]