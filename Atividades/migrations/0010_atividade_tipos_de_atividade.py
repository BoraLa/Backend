# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Atividades', '0009_tipodeatividade'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='tipos_de_atividade',
            field=models.ManyToManyField(to='Atividades.TipoDeAtividade'),
        ),
    ]
