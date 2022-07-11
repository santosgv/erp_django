from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import  redirect, render
from django.contrib import auth
from .utils import email_html
from hashlib import sha256


def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'cadastro.html')

    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')

def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'logar.html')



def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')
