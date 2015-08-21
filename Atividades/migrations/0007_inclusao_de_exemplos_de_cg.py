# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
from Atividades.models import Atividade
from Atividades.models import Categoria

def lancar_atividade(*varios_parametros):
	pass

class Migration(migrations.Migration):

    dependencies = [
        ('Atividades', '0006_auto_20150821_1438'),
    ]

    operations = [
    	migrations.RunPython(lancar_atividade)
    ]