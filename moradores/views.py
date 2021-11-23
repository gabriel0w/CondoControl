from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from datetime import datetime


def residentes(request, apartamento):
	morador = residente.objects.filter(apto__apto = apartamento)
	funcionario = prestador.objects.filter(apto__apto = apartamento)
	movimentacao = movimento.objects.filter(apto__apto = apartamento).values_list('entrada','pessoa__nome')
	return render(request, 'hello.html', {'morador':morador, 'apartamento':apartamento, 'prestador':funcionario, 'movimentacao':movimentacao})

def prestadores(request, pk):
	funcionario = prestador.objects.get(id = pk)
	movimentacao = movimento.objects.filter(pessoa__nome = funcionario).values_list('entrada', flat=True)
	return render(request, 'prestadores.html', {'funcionario':funcionario, 'movimentacao':movimentacao})

def apartamentos(request):
	apto_a = apto.objects.filter(bloco = 'A')
	apto_b = apto.objects.filter(bloco = 'B')
	return render(request, 'aptos.html', {'apto_a':apto_a, 'apto_b':apto_b})

def morador(request, pk):
	morador = residente.objects.get(id = pk)
	movimentacao = movimento.objects.filter(pessoa__nome = morador).values_list('entrada', flat=True)
	return render(request, 'morador.html', {'morador':morador, 'movimentacao':movimentacao})