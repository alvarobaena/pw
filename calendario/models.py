from django.db import models
from lnfsapp.models import Equipo, Jugador

# Create your models here.

class Jornada(models.Model):
	numero=models.IntegerField(default=0)
	def __unicode__(self):
		return unicode (self.numero)

class Partido(models.Model):
	equipoLocal=models.ForeignKey(Equipo,related_name='Local')
	equipoVisit=models.ForeignKey(Equipo,related_name='Visitante')
	fechaInicio=models.DateTimeField()
	resultado=models.CharField(max_length=10)
	jornada=models.ForeignKey(Jornada)
	enjuego="En juego"
	noempezado="Sin comenzar"
	finalizado="Finalizado"
	opsituacion=((enjuego, 'En juego'), (noempezado, 'Sin comenzar'), (finalizado, 'Finalizado'))
	situacion=models.CharField(max_length=30, choices=opsituacion)
	def __unicode__(self):
		return self.equipoLocal.nombre+"-"+self.equipoVisit.nombre
