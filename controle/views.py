from django.shortcuts import render
from .models import Estoque, Venda, Produto


def categorias(request):

    return render(request,'categoria.html')

def produtos(request):

    return render(request,'produtos.html')

def estoque(request):
    if request.method == "GET":
        estoques = Estoque.objects.all()
        return render(request,'estoque.html', {'estoques': estoques})



def vendas(request):
    return render(request,'vendas.html')

def fornecedores(request):
    return render(request,'fornecedores.html')

def pessoas(request):
    return render(request,'pessoas.html')