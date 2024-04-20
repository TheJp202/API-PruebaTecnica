from django.urls import path
from .views import CargoLC_APIView,CargoRUD_APIView

urlpatterns = [
    path('list_create/',CargoLC_APIView.as_view(),name='crear_listar_cargo'),
    path('update_delete/<int:pk>',CargoRUD_APIView.as_view(),name='eliminar_actualizar_cargo')
]