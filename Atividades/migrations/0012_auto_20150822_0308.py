# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Atividades.models import *
from django.db import models, migrations
import random
from itertools import combinations

def vincular_tipos(*params):
	corrida = TipoDeAtividade.objects.get(nome="Corrida")
	patins = TipoDeAtividade.objects.get(nome="Patins")
	skate = TipoDeAtividade.objects.get(nome="Skate")
	piquinique = TipoDeAtividade.objects.get(nome="Piquenique")
	basquete = TipoDeAtividade.objects.get(nome="Basquete")

	combinacoes = list(combinations([corrida, patins, skate, piquinique, basquete], 2))

	for atividade in Atividade.objects.all():
		atividade.tipos_de_atividade.add(*random.choice(combinacoes))
		atividade.save()

class Migration(migrations.Migration):

    dependencies = [
        ('Atividades', '0011_auto_20150822_0251'),
    ]

    operations = [
    	migrations.RunPython(vincular_tipos)
    ]
