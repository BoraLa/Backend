from django.db import models

class Atividade(models.Model):
	nome = models.CharField(max_length=200)
	descricao = models.CharField(max_length=1000)
	url = models.URLField(default='http://thumbs.dreamstime.com/t/skyline-gen%C3%A9rica-da-cidade-30807534.jpg')