# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Atividades', '0004_criacao_das_categorias'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='categoria',
            field=models.ForeignKey(default=2, to='Atividades.Categoria'),
        ),
    ]
