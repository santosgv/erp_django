from datetime import datetime
from tkinter import CASCADE
from django.contrib.auth.models import User
from django.db import models



class Empresa(models.Model):
    Estado_choices = (   ('AC','AC'),
                         ('AL','AL'),
                         ('AP','AP'),
                         ('AM','AM'),
                         ('BA','BA'),
                         ('CE','CE'),
                         ('ES','ES'),
                         ('GO','GO'),
                         ('MA','MA'),
                         ('MT','MT'),
                         ('MS','MS'),
                         ('MG','MG'),
                         ('PA','PA'),
                         ('PB','PB'),
                         ('PR','PR'),
                         ('PE','PE'),
                         ('PI','PI'),
                         ('RJ','RJ'),
                         ('RN','RN'),
                         ('RS','RS'),
                         ('RO','RO'),
                         ('RR','RR'),
                         ('SC','SC'),
                         ('SP','SP'),
                         ('SE','SE'),
                         ('TO','TO'),
                         ('DF','DF'))


    DATA_CADASTRO = datetime.now()
    NOME_EMPRESA = models.CharField(max_length=200)
    CPF_CNPJ = models.CharField(max_length=200)
    CEP = models.CharField(max_length=10)
    ENDERECO =models.CharField(max_length=200)
    BAIRRO = models.CharField(max_length=200)
    NUMERO =models.CharField(max_length=6)
    COMPLEMENTO =models.CharField(max_length=100)
    CIDADE = models.CharField(max_length=200)
    ESTADO =models.CharField(max_length=2 , choices=Estado_choices)
    RESPONSAVEL = models.CharField( max_length=500 ,blank=True)
    EMAIL_RESPONSAVEL = models.EmailField()
    EMAIL_FINANCEIRO = models.EmailField()
    OBS =models.TextField(max_length=500 ,blank=True)
    def __str__(self) -> str:
        return self.NOME_EMPRESA

class UsuarioEmpresa(models.Model):
    USUARIO = models.ForeignKey(User , on_delete=models.CASCADE, null=True)
    EMPRESA = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.USUARIO









