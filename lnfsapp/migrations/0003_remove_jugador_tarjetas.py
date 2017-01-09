# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lnfsapp', '0002_auto_20161105_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jugador',
            name='tarjetas',
        ),
    ]
