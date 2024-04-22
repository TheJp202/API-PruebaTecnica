from django.urls import path
from .views import EstudianteNotaLC_APIView,EstudianteNotaRUD_APIView,ObtenerIdEvaluacionAPIView,EstudianteNotaUpdateAPIView

urlpatterns = [
    path('list_create/',EstudianteNotaLC_APIView.as_view(),name='crear_listar_estudiante_nota'),
    path('update_delete/<int:pk>',EstudianteNotaRUD_APIView.as_view(),name='eliminar_actualizar_estudiante_nota'),
    path('only_update/<int:pk>',EstudianteNotaUpdateAPIView.as_view(),name='actualizar_nota'),
    path('evaluation/<str:dni>/<str:curso>/<str:elemento>',ObtenerIdEvaluacionAPIView.as_view(),name='evaluacion')
]