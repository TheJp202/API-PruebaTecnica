from django.urls import path
from .views import EmpleadoL_APIView,RegisterAPIView,LoginAPIView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('list/',EmpleadoL_APIView.as_view(),name='listar_empleado'),
    path('register/', csrf_exempt(RegisterAPIView.as_view()), name='register'),
    path('login/', csrf_exempt(LoginAPIView.as_view()), name='login'),

]