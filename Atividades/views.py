from django.shortcuts import render
from django.http import JsonResponse
from Atividades.models import Atividade
import random

def obter_todas_as_atividades(requisicao):
	campos = ['nome', 'descricao', 'id', 'url', 'endereco', 'categoria__nome']
	atividades = list(Atividade.objects.all().values(*campos))
	random.shuffle(atividades)
	return JsonResponse({'atividades': atividades})