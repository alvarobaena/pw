# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('nombreUrl', models.CharField(max_length=50)),
                ('entrenador', models.CharField(max_length=50)),
                ('pabellon', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('escudo', models.ImageField(upload_to=b'')),
                ('ano', models.IntegerField(default=0)),
                ('historia', models.TextField(max_length=650)),
                ('puntos', models.IntegerField(default=0)),
                ('partidosJugados', models.IntegerField(default=0)),
                ('partidosGanados', models.IntegerField(default=0)),
                ('partidosPerdidos', models.IntegerField(default=0)),
                ('partidosEmpatados', models.IntegerField(default=0)),
                ('golesAfavor', models.IntegerField(default=0)),
                ('golesAcontra', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=80)),
                ('edad', models.IntegerField(default=0)),
                ('goles', models.IntegerField(default=0)),
                ('tarjetas', models.IntegerField(default=0)),
                ('dorsal', models.IntegerField(default=0)),
                ('fechaNacimiento', models.DateField()),
                ('paisOrigen', models.CharField(max_length=50)),
                ('posicion', models.CharField(max_length=30, choices=[(b'Delantero', b'Delantero'), (b'Centrocampista', b'Centrocampista'), (b'Defensa', b'Defensa'), (b'Portero', b'Portero')])),
                ('equipo', models.ForeignKey(to='lnfsapp.Equipo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
