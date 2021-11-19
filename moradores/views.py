from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def moradores(request):
	pessoas = pessoa.objects.all()
	return render(request, 'hello.html', {'pessoas':pessoas})

def prestadores(request):
	prestadores = prestador.objects.all()
	return render(request, 'prestadores.html', {'prestadores':prestadores})

def morador(request, pk):
	morador = pessoa.objects.get(id = pk)
	return render(request, 'morador.html', {'morador':morador})