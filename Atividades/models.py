from django.db import models

class Atividade(models.Model):
	nome = models.CharField(max_length=200)
	descricao = models.CharField(max_length=1000)