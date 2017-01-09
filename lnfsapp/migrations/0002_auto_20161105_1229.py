# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lnfsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='posicion',
            field=models.CharField(max_length=30, choices=[(b'Pivot', b'Pivot'), (b'Ala', b'Ala'), (b'Cierre', b'Cierre'), (b'Portero', b'Portero')]),
            preserve_default=True,
        ),
    ]
