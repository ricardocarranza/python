from django.db import models

# Create your models here.

class TipoEquipo(models.Model):
	tipo_de_equipo = models.CharField(max_length=75)

	def __unicode__(self):
		return self.tipo_de_equipo

class Estado(models.Model):
	estado = models.CharField(max_length=75)

	def __unicode__(self):
		return self.estado

class Unidad(models.Model):
	unidad_optica = models.CharField(max_length=75)

	def __unicode__(self):
		return self.unidad_optica

class Equipo(models.Model):
	pc = models.CharField(max_length=75)
	usuario = models.CharField(null=True, blank=True, max_length=75)
	estado = models.ForeignKey(Estado)
	fecha = models.DateField()
	tipo_de_equipo = models.ForeignKey(TipoEquipo)
	serie_caja = models.CharField(max_length=75)
	modelo = models.CharField(max_length=75)
	moderboard_marca = models.CharField(max_length=75)
	moderboard_tipo = models.CharField(max_length=75)
	moderboard_modelo = models.CharField(max_length=75)
	ram_marca = models.CharField(max_length=50)
	ram_capacidad = models.CharField(max_length=30)
	ram_slot = models.CharField(max_length=30)
	fuente_marca = models.CharField(max_length=50)
	fuente_potencia = models.CharField(max_length=30)
	fuente_pines = models.CharField(max_length=30)
	disco_duro_marca  = models.CharField(max_length=75)
	disco_duro_capacidad  = models.CharField(max_length=30)
	disco_duro_interfaz  = models.CharField(max_length=30)
	procesador_marca  = models.CharField(max_length=75)
	procesador_referencia  = models.CharField(max_length=30)
	procesador_interfaz  = models.CharField(max_length=30)
	unidades_opticas  = models.ManyToManyField(Unidad)



