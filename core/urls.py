
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cargo/',include('Cargo.urls')),
    path('empleado/',include('Empleado.urls')),
    path('estudiante/',include('Estudiante.urls')),
    path('bloque/',include('Bloque.urls')),
    path('curso/',include('Curso.urls')),
    path('elemento/',include('Elemento.urls')),
    path('cargo_empleado/',include('CargoEmpleado.urls')),
    path('bloque_curso/',include('BloqueCurso.urls')),
    path('curso_elemento/',include('CursoElemento.urls')),
    path('estudiante_bloque/',include('EstudianteBloque.urls')),
    path('bloque_curso_profesor/',include('BloqueCursoProfesor.urls')),
    path('bloque_cuota/',include('BloqueCuota.urls')),
    path('estudiante_nota/',include('EstudianteNota.urls'))
]
