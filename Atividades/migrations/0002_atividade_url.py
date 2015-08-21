# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Atividades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='url',
            field=models.URLField(default='http://thumbs.dreamstime.com/t/skyline-gen%C3%A9rica-da-cidade-30807534.jpg'),
        ),
    ]
