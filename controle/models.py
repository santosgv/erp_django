from datetime import datetime
from django.db import models


class Categoria(models.Model):
    categoria = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.categoria

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.FloatField()
    categoria = models.ForeignKey(Categoria ,blank=True ,null=True ,on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome

class Estoque(models.Model):
    produto = models.ForeignKey(Produto ,on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField()

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(blank=True ,null=True ,max_length=18)
    telefone = models.CharField(blank=True ,null=True ,max_length=15)
    categoria = models.ForeignKey(Categoria ,blank=True ,null=True ,on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(blank=True ,null=True ,max_length=15)
    cpf = models.CharField(max_length=12)
    email= models.EmailField()
    CEP = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=200)
    Numero = models.CharField(max_length=5)
    Complemento = models.CharField(max_length=50)
    Bairro = models.CharField(max_length=50)
    Cidade = models.CharField(max_length=50)
    Estado = models.CharField(max_length=2)

    def __str__(self) -> str:
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=12)
    telefone = models.CharField(blank=True ,null=True ,max_length=15)
    email = models.EmailField()
    CLT = models.CharField(max_length=100)
    CEP = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=200)
    Numero = models.CharField(max_length=5)
    Complemento = models.CharField(max_length=50)
    Bairro = models.CharField(max_length=50)
    Cidade = models.CharField(max_length=50)
    Estado = models.CharField(max_length=2)

    def __str__(self) -> str:
        return self.nome

class Venda(models.Model):
    itensvendidos = models.ManyToManyField(Produto)
    vendedor = models.ForeignKey(Funcionario ,on_delete=models.DO_NOTHING)
    comprador = models.ForeignKey(Pessoa,blank=True ,null=True ,on_delete=models.DO_NOTHING)
    quantidade_vendida= models.IntegerField()
    data = models.DateTimeField(default=datetime.now())

