from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def say_hello(request):
	pessoas = pessoa.objects.all()
	return render(request, 'hello.html', {'pessoas':pessoas, })
