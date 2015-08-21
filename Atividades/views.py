from django.shortcuts import render
from django.http import JsonResponse
from Atividades.models import Atividade

def obter_todas_as_atividades(requisicao):
	campos = ['nome', 'descricao', 'id', 'url', 'endereco', 'categoria__nome']
	atividades = Atividade.objects.all().values(*campos)
	return JsonResponse({'atividades': list(atividades)})