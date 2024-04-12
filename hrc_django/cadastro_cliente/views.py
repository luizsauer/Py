from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não está logado! ')
        return redirect('login')
    else:
        return HttpResponse('Teste do index')