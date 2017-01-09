from django.db import models

# Create your models here.

class Equipo(models.Model):
	nombre=models.CharField(max_length=50)
	nombreUrl=models.CharField(max_length=50)
	entrenador=models.CharField(max_length=50)
	pabellon=models.CharField(max_length=50)
	ciudad=models.CharField(max_length=50)
	escudo=models.ImageField()
	ano=models.IntegerField(default=0)
	historia=models.TextField(max_length=650)
	puntos=models.IntegerField(default=0)
	partidosJugados=models.IntegerField(default=0)
	partidosGanados=models.IntegerField(default=0)
	partidosPerdidos=models.IntegerField(default=0)
	partidosEmpatados=models.IntegerField(default=0)
	golesAfavor=models.IntegerField(default=0)
	golesAcontra=models.IntegerField(default=0)
	def __unicode__(self):
		return self.nombre

class Jugador(models.Model):
	nombre=models.CharField(max_length=80)
	edad=models.IntegerField(default=0)
	goles=models.IntegerField(default=0)
	equipo=models.ForeignKey(Equipo)
	dorsal=models.IntegerField(default=0)
	fechaNacimiento=models.DateField()
	paisOrigen=models.CharField(max_length=50)
	pivot="Pivot"
	ala="Ala"
	cierre="Cierre"
	portero="Portero"
	opposiciones=((pivot, 'Pivot'), (ala, 'Ala'), (cierre, 'Cierre'), (portero, 'Portero'))
	posicion=models.CharField(max_length=30, choices=opposiciones)
	def __unicode__(self):
		return self.nombre	
