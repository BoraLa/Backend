# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from Atividades.models import Categoria

def criar_categorias(apps, schema_editor):
	Categoria.objects.create(nome="Esporte")
	Categoria.objects.create(nome="Cultura")
	Categoria.objects.create(nome="Lazer")

class Migration(migrations.Migration):

    dependencies = [
        ('Atividades', '0003_categoria'),
    ]

    operations = [
    	migrations.RunPython(criar_categorias)
    ]
