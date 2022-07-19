from django.contrib import admin
from .models import Produto,Pessoa , Venda,Fornecedor,Funcionario,Estoque, Categoria


admin.site.register(Produto)
admin.site.register(Pessoa)
admin.site.register(Venda)
admin.site.register(Fornecedor)
admin.site.register(Funcionario)
admin.site.register(Estoque)
admin.site.register(Categoria)