from .models import *
from rest_framework import serializers

class AutosSerializer (serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Autos
		fields = ('placa', 'marca_id', 'tipo_id')


class PropietariosSerializer (serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Propietarios
		fields = ('nombre', 'cedula')

class MarcasSerializer (serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Marcas
		fields = ('nombre')

class TiposSerializer (serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Tipos
		fields = ('nombre_tipo')




