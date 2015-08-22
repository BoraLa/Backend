# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Atividades', '0008_auto_20150821_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDeAtividade',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
    ]
