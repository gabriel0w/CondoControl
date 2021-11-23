from django.db import models

# Create your models here.

class pessoa(models.Model):
	nome = models.CharField(max_length=200, null=True)
	telefone = models.CharField(max_length=11, null=True)
	cpf = models.CharField(max_length=11, null=True)
	email = models.CharField(max_length=100, null=True)
	foto = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.nome

class apto(models.Model):
	apto = models.CharField(max_length=3, null=True)
	bloco = models.CharField(max_length=1, null=True)

	def __str__(self):
		return self.apto

class residente(models.Model):
	nome = models.ForeignKey(pessoa, null=True, on_delete=models.SET_NULL)
	apto = models.ForeignKey(apto, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.nome.nome

class prestador(models.Model):
	nome = models.ForeignKey(pessoa, null=True, on_delete=models.SET_NULL)
	apto = models.ManyToManyField(apto)

	def __str__(self):
		return self.nome.nome

class movimento(models.Model):
	entrada = models.DateTimeField(editable=True)
	saída = models.DateTimeField(editable=True, null=True, blank=True)
	pessoa = models.ForeignKey(pessoa, null=True, on_delete=models.SET_NULL)
	apto = models.ForeignKey(apto, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.pessoa.nome