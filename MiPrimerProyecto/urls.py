"""
URL configuration for MiPrimerProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework import routers

from catalogos.views import PaisViewSet
from catalogos.views import DepartamentoViewSet
from catalogos.views import MunicipioViewSet

router = routers.DefaultRouter()
router.register(r'pais', PaisViewSet)
router.register(r'departamento', DepartamentoViewSet)
router.register(r'Municipio', MunicipioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("customauthentication.urls")),
    path('', include("home.urls")),
    path('catalogos/', include("catalogos.urls")),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]