# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lnfsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaInicio', models.DateTimeField()),
                ('resultado', models.CharField(max_length=10)),
                ('situacion', models.CharField(max_length=30, choices=[(b'En juego', b'En juego'), (b'Sin comenzar', b'Sin comenzar'), (b'Finalizado', b'Finalizado')])),
                ('equipoLocal', models.ForeignKey(related_name='Local', to='lnfsapp.Equipo')),
                ('equipoVisit', models.ForeignKey(related_name='Visitante', to='lnfsapp.Equipo')),
                ('jornada', models.ForeignKey(to='calendario.Jornada')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
