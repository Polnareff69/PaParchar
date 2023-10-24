from django.contrib import admin
from django.urls import path, include
from usuarios import views as usuariosVista
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('login_user', usuariosVista.login_user, name='login_user'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
