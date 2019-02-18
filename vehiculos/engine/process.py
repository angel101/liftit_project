from ..models import *


from django.db.models import Q
from django.db.models import Count

# PROPIETATIOS METHODS ==================================================================

def create_propietario_process(request):
	propietario = Propietarios(nombre = request['nombre'], cedula = request['cedula'])
	propietario.save()
	return propietario



def list_propietario_process():
	propietarios = Propietarios.objects.all().values()
	return list(propietarios)




# VEHICULOS METHODS ==================================================================

def create_vehiculos_process(request):
	auto = Autos(placa = request['placa'], marca_id = request['marca_id'], tipo_id = request['tipo_id'])
	auto.save()
	return auto



def list_vehiculos_process():
	autos = Autos.objects.all().values()
	return list(autos)


def report_vehiculos_process():
	vehiculos = Autos.objects.all().values('placa', 'marca__nombre','tipo__nombre').order_by('marca__nombre')
	return list(vehiculos)

# MARCA  METHODS ==================================================================

def create_marcas_process(request):
	marca = Marcas(nombre = request['nombre'])
	marca.save()
	return marca



def list_marcas_process():
	marcas = Marcas.objects.all().values()
	return list(marcas)



def report_marcas_process():
	autos = Autos.objects.values('marca__nombre').annotate(count_marca=Count('marca')).order_by()
	return list(autos)



# TIPOS  METHODS ==================================================================

def create_tipos_process(request):
	tipo = Tipos(monbre = request['nombre'])
	tipo.save()
	return tipo



def list_tipos_process():
	tipos = Tipos.objects.all().values()
	return list(tipos)


# FINDER METHODS =================================================================
def finder(request):
	query = request['query']

	auto = Auto_propietarios.objects.values('auto__placa','auto__marca__nombre','auto__tipo__nombre').filter(Q(auto__placa__contains = query) | Q(auto__marca__nombre__contains = query) | Q(auto__tipo__nombre__contains = query) | Q(propietario__nombre__contains = query) | Q(propietario__cedula__contains = query))
	return list(auto)