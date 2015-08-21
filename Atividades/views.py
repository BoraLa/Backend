from django.shortcuts import render
from django.http import JsonResponse
from Atividades.models import Atividade

def obter_todas_as_atividades(requisicao):
	atividades = Atividade.objects.all().values('nome', 'descricao', 'id', 'url', 'endereco')
	return JsonResponse({'atividades': list(atividades)})