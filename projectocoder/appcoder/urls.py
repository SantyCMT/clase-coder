from django.urls import path
from appcoder.views import *

urlpatterns = [
    path("Inicio/pagina-inicio", inicio, name="coder-inicio"),
    path("Estudiantes/listado", Estudiantes, name="coder-estudiantes"),
    path("Profesor/", Profesor, name="coder-profesor"),
    path("Curso/", Curso, name="coder-curso"),
    path("Catedra/", Catedra, name="coder-catedra"),
    path("Entrega/", Entrega, name="coder-entrega"),
]