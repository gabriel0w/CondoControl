from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def residentes(request, apartamento):
	morador = residente.objects.filter(apto__apto = apartamento)
	funcionario = prestador.objects.filter(apto__apto = apartamento)
	return render(request, 'hello.html', {'morador':morador, 'apartamento':apartamento, 'prestador':funcionario})

def prestadores(request):
	prestadores = prestador.objects.all()
	return render(request, 'prestadores.html', {'prestadores':prestadores})

def morador(request, pk):
	morador = pessoa.objects.get(id = pk)
	return render(request, 'morador.html', {'morador':morador})