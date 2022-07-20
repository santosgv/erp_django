from django.shortcuts import redirect, render
from .models import Estoque, Venda, Produto, Categoria


def categorias(request):

    return render(request,'categoria.html')

def produtos(request):
    if request.method == "GET":
        Produtos = Produto.objects.all()
    return render(request,'produtos.html',{'Produtos':Produtos})

def inserirProduto(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        return render(request,'inserirProduto.html',{'categorias':categorias})
    else:
        Produtos = Produto.objects.all()
        nome = request.POST.get('Nome')
        preco = request.POST.get('PRECO')
        categoria = request.POST.get('categoria')

        produto = Produto(nome =nome,preco=preco,categoria=Categoria.objects.get(id=categoria)

        )
        produto.save()
        return render(request,'produtos.html',{'Produtos':Produtos})

def estoque(request):
    if request.method == "GET":
        estoques = Estoque.objects.all()
        return render(request,'estoque.html', {'estoques': estoques})

def inserirEstoque(request):
    if request.method == "GET":
        produtos = Produto.objects.all()
        return render(request,'inserirEstoque.html',{'produtos':produtos})
    else:
        produto = request.POST.get('produto')
        produto_id =Produto.objects.get(id=produto)
        qtd = request.POST.get('quantidade')

        
        estoque = Estoque(produto=Produto.objects.get(id=produto_id.id),
        quantidade = qtd
        )
        estoque.save()
        return redirect('/controle/estoque')

def vendas(request):
    return render(request,'vendas.html')

def pessoas(request):
    return render(request,'pessoas.html')