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

def tipos_de_atividade_por_atividade(requisicao, id):
	atividade = Atividade.objects.get(id=id)
	tipos = atividade.tipos_de_atividade.all().values('nome')
	return JsonResponse({'tipos_de_atividade': list(tipos)})

def busca_de_atividades(requisicao):
	termo = requisicao.GET['termo']
	atividades_encontradas = \
		Atividade.objects.filter(nome__icontains=termo) | \
		Atividade.objects.filter(descricao__icontains=termo) | \
		Atividade.objects.filter(tipos_de_atividade__nome__icontains=termo)
	return obter_atividades(atividades_encontradas.distinct())

def obter_atividades(dados):
	campos = ['nome', 'descricao', 'id', 'url', 'endereco', 'categoria__nome']
	atividades = list(dados.values(*campos))
	random.shuffle(atividades)
	return JsonResponse({'atividades': atividades})