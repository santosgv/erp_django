from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logar/', views.logar, name='logar'),
    path('sair/', views.sair, name="sair"),
]