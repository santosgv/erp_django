from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import  redirect, render
from django.contrib import auth



def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')

    elif request.method == "POST":
        
        return render(request, 'cadastro.html')

def logar(request):
    if request.method == "GET":
        return render(request, 'logar.html')



def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')
