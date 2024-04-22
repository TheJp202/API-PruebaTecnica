from django.urls import path
from .views import EstudianteLC_APIView,EstudianteRUD_APIView,ObtenerResultadoProfesorAPIView,ObtenerResultadoAdminAPIView,ObtenerResultadoAdminProAPIView,CrearEstudianteConBloqueAPIView

urlpatterns = [
    path('list_create/',EstudianteLC_APIView.as_view(),name='crear_listar_estudiante'),
    path('update_delete/<int:pk>',EstudianteRUD_APIView.as_view(),name='eliminar_actualizar_estudiante'),
    path('list_profesor/<int:id_profesor>/', ObtenerResultadoProfesorAPIView.as_view(), name='obtener_resultado'),
    path('list_admin/', ObtenerResultadoAdminAPIView.as_view(), name='obtener_resultado'),
    path('lis_admin_pro/', ObtenerResultadoAdminProAPIView.as_view(), name='obtener_resultado'),
    path('only_create/<str:nombre>/<str:apellido>/<str:dni>/<str:telefono>/<str:correo>/<str:contraseña>/<str:bloque>',CrearEstudianteConBloqueAPIView.as_view())

]   