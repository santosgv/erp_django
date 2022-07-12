from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse
from django.shortcuts import  redirect, render
from .models import Empresa ,Usuario



def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')

    elif request.method == "POST":

        NOME_EMPRESA = request.POST.get("NOME_EMPRESA")
        CPF_CNPJ = request.POST.get("CPF_CNPJ")
        CEP = request.POST.get("CEP")
        ENDERECO = request.POST.get("ENDERECO")
        BAIRRO = request.POST.get("BAIRRO")
        NUMERO = request.POST.get("NUMERO")
        COMPLEMENTO = request.POST.get("COMPLEMENTO")
        CIDADE = request.POST.get("CIDADE")
        ESTADO = request.POST.get("ESTADO")
        EMAIL_RESPONSAVEL = request.POST.get("EMAIL_RESPONSAVEL")
        EMAIL_FINANCEIRO = request.POST.get("EMAIL_FINANCEIRO")
        OBS = request.POST.get("OBS")

    

        empresa = Empresa(
            NOME_EMPRESA = NOME_EMPRESA,
            CPF_CNPJ = CPF_CNPJ,
            CEP = CEP,
            ENDERECO = ENDERECO,
            BAIRRO = BAIRRO,
            NUMERO = NUMERO,
            COMPLEMENTO = COMPLEMENTO,
            CIDADE = CIDADE,
            ESTADO = ESTADO,
            RESPONSAVEL = NOME_EMPRESA,
            EMAIL_RESPONSAVEL = EMAIL_RESPONSAVEL,
            EMAIL_FINANCEIRO = EMAIL_FINANCEIRO,
            OBS = OBS)
        
        empresa.save()

        usuario_root = Usuario.objects.create(username=NOME_EMPRESA , first_name=CPF_CNPJ,email=EMAIL_RESPONSAVEL,ID_EMPRESA= Empresa.objects.get(id=empresa.id))
        usuario_root.save()

 
        
        return HttpResponse('Foii')

def logar(request):
    if request.method == "GET":
        return render(request, 'logar.html')



def sair(request):
    return redirect('/auth/logar')
