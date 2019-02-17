from django import forms
from .models import *

class PropietarioForm(forms.ModelForm):
	class Meta:
		model = Propietarios
		fields = ('nombre', 'cedula', 'document', )

class MarcaForm(forms.ModelForm):
	class Meta:
		model = Marcas
		fields = ('nombre',)

class TipoForm(forms.ModelForm):
	class Meta:
		model = Tipos
		fields = ('nombre',)


class VehiculoForm(forms.ModelForm):
	class Meta:
		model = Autos
		fields = ('placa', 'marca','tipo',)

class Vehiculo_propietarioForm(forms.ModelForm):
	class Meta:
		model = Auto_propietarios
		fields = ('auto', 'propietario',)