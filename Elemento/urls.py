from django.urls import path
from .views import ElementoLC_APIView,ElementoRUD_APIView

urlpatterns = [
    path('list_create/',ElementoLC_APIView.as_view(),name='crear_listar_elemento'),
    path('update_delete/<int:pk>',ElementoRUD_APIView.as_view(),name='eliminar_actualizar_elemento')
]