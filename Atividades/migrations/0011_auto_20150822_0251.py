# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
from Atividades.models import TipoDeAtividade

def lancar_tipos(*parametros):
	TipoDeAtividade.objects.create(nome="Corrida")
	TipoDeAtividade.objects.create(nome="Patins")
	TipoDeAtividade.objects.create(nome="Skate")
	TipoDeAtividade.objects.create(nome="Piquenique")
	TipoDeAtividade.objects.create(nome="Basquete")

class Migration(migrations.Migration):

    dependencies = [
        ('Atividades', '0010_atividade_tipos_de_atividade'),
    ]

    operations = [
    	migrations.RunPython(lancar_tipos)
    ]
