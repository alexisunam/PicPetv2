"""koala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from picpet.views import home
from picpet.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('iniciar_sesion', iniciarSesion, name='iniciar sesion'),
    path('validarSesion', validarSesion, name='validar sesion'),
    path('cuentas', cuentas, name='cuentas'),
    path('registrar_artista', registrarArtista, name='registrar artista'),
    path('registrar_persona', registrarPersona, name='registrar persona'),
    path('insertarPersona', insertarPersona, name='insertarPersona'),
    path('insertarArtista', insertarArtista, name='insertarArtista'),
    path('Consultar_clientes', readPersonas, name='consultar clientes'),
    path('mi_perfil/<int:id>', mostrarUsuario, name='mi perfil'),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )