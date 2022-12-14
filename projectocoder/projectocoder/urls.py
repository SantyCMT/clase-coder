"""projectocoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unittest.mock import patch
from django.contrib import admin
from django.urls import path, include
from projectocoder.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', vista_saludo),
    path('login/', iniciar_sesion ),
    path('hoy/<nombre>/', dia_hoy),
    path('nacimiento/<edad>/', calcular_año),
    path('inicio/', vista_plantilla2),
    path("alumnos/", vista_listado_alumnos2),

    path("coder/", include("appcoder.urls"))


]
