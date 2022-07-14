from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse
from django.shortcuts import  redirect, render
from .models import Empresa, UsuarioEmpresa 
from django.contrib.auth.models import User
from django.contrib import auth 



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

        if len(NOME_EMPRESA.strip()) == 0 or len(CPF_CNPJ.strip()) == 0 or len(EMAIL_RESPONSAVEL.strip()) ==0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/auth/cadastro')
    try:

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

            senha ='Senha123@'

            user = User.objects.create_user(username=NOME_EMPRESA,
                                            email = EMAIL_RESPONSAVEL,
                                            password=senha)
            user.save()

            usuario_empresa = UsuarioEmpresa(
            USUARIO =User.objects.get(id=user.id),
            EMPRESA = Empresa.objects.get(id=empresa.id)
        )

            usuario_empresa.save()
        
            return HttpResponse('Foii')
    except:
            pass


def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')

        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect('/auth/logar')
        else:
            auth.login(request, usuario)
            return redirect('/')



def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')
