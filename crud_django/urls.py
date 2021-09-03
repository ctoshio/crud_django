"""crud_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from aplicaciones.principal.views import crearPersona, inicio, editarPersona, eliminarPersona
from aplicaciones.principal.class_view import PersonaList, PersonaCreate, PersonaUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',PersonaList.as_view(),name = 'index'),
    path('create_persona/',PersonaCreate.as_view(),name = 'create_persona'),#name could be any name
    path('edit_persona/<int:pk>/',PersonaUpdate.as_view(), name = 'edit_persona'),
    path('delete_persona/<int:id>/',eliminarPersona, name = 'delete_persona'),
]
