from . import views
from django.urls import path


urlpatterns = [
    path('categorias', views.categorias, name='categorias'),
    path('produtos', views.produtos, name='produtos'),
    path('estoque', views.estoque, name='estoque'),
    path('inserirEstoque',views.inserirEstoque, name='inserirEstoque'),
    path('vendas', views.vendas, name='vendas'),
    path('fornecedores', views.fornecedores, name='fornecedores'),
    path('pessoas', views.pessoas, name='pessoas'),
]