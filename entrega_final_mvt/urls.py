"""entrega_final_mvt URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from entrega_final_app.views import mostrar_notas, alta_notas, BuscarNotas, mostrar_usuarios, alta_usuarios, BuscarUsuarios, mostrar_elementos, alta_elementos, BuscarElementos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notas/',mostrar_notas, name = "notas"),
    path('notas/create',alta_notas, name = "notas-create"),
    path('notas/list', BuscarNotas.as_view(), name = "notas-list"),
    path('usuarios/',mostrar_usuarios, name = "usuarios"),
    path('usuarios/create',alta_usuarios, name = "usuarios-create"),
    path('usuarios/list', BuscarUsuarios.as_view(), name = "usuarios-list"),
    path('elementos/',mostrar_elementos, name = "elementos"),
    path('elementos/create',alta_elementos, name = "elementos-create"),
    path('elementos/list', BuscarElementos.as_view(), name = "categoria-list"),
]

