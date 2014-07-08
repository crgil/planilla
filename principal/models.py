from django.db import models
from django.contrib import admin
from datetime import datetime
from django.contrib.auth.models import User, check_password

# Create your models here.

class empresa (models.Model):
	nombre = models.CharField(max_length=200)
	fecha_creacion = models.DateTimeField('Fecha de Creacion')
	direccion = models.CharField(max_length=200)
	telefono1 = models.IntegerField()
	telefono2 = models.IntegerField()

	def __unicode__(self):
		return self.nombre
		return self.fecha_creacion
		return self.direccion
		return self.telefono1
		return self.telefono2

class cargo (models.Model):
	cargo = models.CharField(max_length = 200)
	descripcion = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.cargo
		return self.descripcion

class unidad_medida(models.Model):
	nombre_u_medida = models.CharField(max_length = 200)
	simbolo = models.CharField(max_length = 5)
	cantxunidad = models.DecimalField(max_digits=10, decimal_places=2)
	
	def __unicode__(self):
		return self.nombre_u_medida
		return self.precio_simbolo
		return self.cantxunidad

class tarea(models.Model):
	nombre_tarea = models.CharField(max_length = 200)
	precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
	unidad_medida = models.ForeignKey(unidad_medida)

	def __unicode__(self):
		return self.nombre_tarea
		return self.precio_unitario

class sector(models.Model):
	nombre_sector = models.CharField(max_length = 200)
	
	def __unicode__(self):
		return self.nombre_sector

class lote(models.Model):
	nombre_lote = models.CharField(max_length = 200)
	sector = models.ForeignKey(sector)

	def __unicode__(self):
		return self.nombre_lote

class planilla(models.Model):
	nombre_planilla = models.CharField(max_length = 200)
	fecha_inicio = models.DateTimeField('Fecha de Inicio')
	fecha_fin = models.DateTimeField('Fecha de Finalizacion')
	descripcion = models.CharField(max_length=300)
	total = models.DecimalField(max_digits=10, decimal_places=2)
	estado = models.IntegerField()

	def __unicode__(self):
		return self.nombre_planilla
		return self.fecha_inicio
		return self.fecha_fin
		return self.descripcion
		return self.total
		return self.estado

class contratista (models.Model):
	nombre = models.CharField(max_length = 100)
	apellido = models.CharField(max_length = 100)
	fecha_nac = models.DateTimeField('Fecha de Nacimiento')
	direccion = models.CharField(max_length = 300)
	telefono_casa = models.IntegerField()
	celular = models.IntegerField()

	def __unicode__(self):
		return self.nombre
		return self.apellido
		return self.fecha_nac
		return self.direccion
		return self.telefono_casa
		return self.celular

class empleado_fijo (models.Model):
	usuario = models.ForeignKey(User)
	nombre = models.CharField(max_length = 100)
	apellido = models.CharField(max_length = 100)
	fecha_nac = models.DateTimeField('Fecha de Nacimiento')
	dpi = models.IntegerField()
	direccion = models.CharField(max_length = 300)
	telefono_casa = models.IntegerField()
	celular = models.IntegerField()
	empresa = models.ForeignKey(empresa)

	def __unicode__(self):
		return self.nombre
		return self.apellido
		return self.fecha_nac
		return self.dpi
		return self.direccion
		return self.telefono_casa
		return self.celular

class empleado_temp (models.Model):
	nombre = models.CharField(max_length = 200)
	fecha_nac = models.DateTimeField('Fecha de Nacimiento')
	celular = models.IntegerField()
	contratista = models.ForeignKey(contratista)
	planilla = models.ForeignKey(planilla)

	def __unicode__(self):
		return self.nombre
		return self.fecha_nac
		return self.celular
		
class diario_planilla (models.Model):
	fecha = models.DateTimeField('Fecha',default=datetime.now(),blank=True)
	empleado_temp = models.ForeignKey(empleado_temp)
	tarea = models.ForeignKey(tarea)
	lote = models.ForeignKey(lote)
	empleado_fijo = models.ForeignKey(empleado_fijo)

	

class tipo_pago (models.Model):
	tipo_pago = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=200)

	def __unicode__(self):
		return self.tipo_pago
		return self.descripcion

class pago (models.Model):
	fecha = models.DateTimeField('Fecha de pago')
	tipo_pago = models.ForeignKey(tipo_pago)
	empleado_temp = models.ForeignKey(empleado_temp)
	monto = models.DecimalField(max_digits=10, decimal_places=2)

	def __unicode__(self):
		return self.fecha
		return self.monto