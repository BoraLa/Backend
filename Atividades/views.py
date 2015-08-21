from django.shortcuts import render
from django.http import JsonResponse
from Atividades.models import Atividade
from Atividades.models import Categoria
import random

def obter_todas_as_atividades(requisicao):
	return obter_atividades(Atividade.objects.all())

def atividades_por_categoria(requisicao, categoria):
	categoria = Categoria.objects.get(nome__iexact=categoria)
	atividades = Atividade.objects.filter(categoria=categoria)
	return obter_atividades(atividades)

def obter_atividades(dados):
	campos = ['nome', 'descricao', 'id', 'url', 'endereco', 'categoria__nome']
	atividades = list(dados.values(*campos))
	random.shuffle(atividades)
	return JsonResponse({'atividades': atividades})