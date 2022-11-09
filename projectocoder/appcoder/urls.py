from django.urls import path
from appcoder.views import *

urlpatterns = [
    path("Estudiantes/", Estudiantes),
    path("Profesor/", Profesor),
    path("Curso/", Curso),
    path("Catedra/", Catedra),
    path("Comicion/", Comicion),
]