# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Atividades', '0005_atividade_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='endereco',
            field=models.CharField(default='Rua nada ver Nº 666', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='atividade',
            name='categoria',
            field=models.ForeignKey(to='Atividades.Categoria'),
        ),
    ]
