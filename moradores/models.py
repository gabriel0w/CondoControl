from django.db import models

# Create your models here.

class apto(models.Model):
	bloco = models.CharField(max_length=1, null=True)
	apto = models.CharField(max_length=3, null=True)

	def __str__(self):
		return self.apto

class pessoa(models.Model):
	nome = models.CharField(max_length=200, null=True)
	telefone = models.CharField(max_length=11, null=True)
	cpf = models.CharField(max_length=11, null=True)
	email = models.CharField(max_length=100, null=True)
	apto = models.ForeignKey(apto, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.nome