from django.db import models

# Create your models here.
class Marcas (models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 20,unique=True)
	def __str__(self):
		return self.nombre

class Tipos (models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 20,unique=True)
	def __str__(self):
		return self.nombre

class Propietarios (models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 60)
	cedula = models.CharField(max_length = 15,unique=True)
	active = models.BooleanField(default = True),
	document = models.FileField(upload_to='documents/',default='settings.MEDIA_ROOT/logos/anonymous.jpg',blank=False)
	def __str__(self):
		return self.nombre

class Autos (models.Model):
	id = models.AutoField(primary_key = True)
	placa = models.CharField(max_length = 6,unique=True)
	marca = models.ForeignKey(Marcas, on_delete = models.CASCADE)
	tipo = models.ForeignKey(Tipos, on_delete = models.CASCADE)
	active = models.BooleanField(default = True)
	def __str__(self):
		return self.placa

class Auto_propietarios (models.Model):
	auto = models.ForeignKey(Autos, on_delete = models.CASCADE)
	propietario = models.ForeignKey(Propietarios, on_delete = models.CASCADE)
	active = models.BooleanField(default = True)

