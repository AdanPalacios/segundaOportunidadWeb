"""core URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from .views import vistaPrincipal
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', login_required(vistaPrincipal.as_view()) , name="Home"),
    path('registroUsuario/', views.registroUsuario, name="registroUsuario"),
    path('login/', LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='pages/login.html'), name='logout'),
    path('ubicacion/', views.ubicacion, name="ubicacion"), 
    path('informacionPersonal/', views.informacionPersonal, name="informacionPersonal"), 
    path('editarInformacionPersonal/', views.editarInfoPersonal, name="editarInfoPersonal"),
    path('recuperarCuenta/', views.recuperarCuenta, name="recuperarCuenta"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
