# DJANGO IMPORTS ==================================================
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Context, Template, loader
from django.core.files.storage import FileSystemStorage

# MODELS IMPORTS ==================================================

from .models import *


# FORMS IMPORT
from .forms import * 

# REST IMPORTS ====================================================
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes


# SEREALIZER IMPORT  ==============================================
from .serializers import *


# HELPER FILE IMPORT ==============================================
from .engine.process import * 

# Create your views here.


def index(request):
	#t = loader.get_template('templates/core/home.html')
	return render(request,template_name='app/base_site.html')



@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def health(request):
	if request.method == 'GET':
		return Response({'message' : 'Api ok'})


# PROPIETARIOS REST =================================================================================================

@api_view(['GET', 'POST'])
def create_propietatios(request):
	if request.method == 'GET':
		return Response({'message' : 'api add Propietatio okey'},status = 200)
	elif request.method == 'POST':
		serializer = PropietariosSerializer(data = request.data)
		if serializer.is_valid():
			try:
				savedObject = create_propietario_process(serializer.data)

				return Response({'message' : 'rest fine'},status = 200)
			except Exception as e:
				return Response({'message' : 'error inserting the object in db', 'error' : str(e)})
		else:
			return Response({'message' : 'rest need params', 'data': serializer.errors},status = 200)
	else:
		return Response({'message' : 'method not suported'},status=405)


@api_view(['GET', 'POST'])
def list_propietatios(request):
	if request.method == 'GET':
		return Response({'message' : 'api list Propietatio okey'},status = 200)
	elif request.method == 'POST':
		try:
			listObjects = list_propietario_process()
			
			return Response({'message' : 'rest fine','data':listObjects},status = 200)
		except Exception as e:
			return Response({'message' : 'error inserting the object in db', 'error' : str(e)})
	else:
		return Response({'message' : 'method not suported'},status=405)




def user_creation_form_upload(request):
	if request.method == 'POST':
		form = PropietarioForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = PropietarioForm()
	return render(request, 'core/creation.html', {
		'form': form
	})




# VEHICULOS REST =======================================================================================================


@api_view(['GET', 'POST'])
def create_vehiculos(request):
	if request.method == 'GET':
		return Response({'message' : 'api add vehiculo okey'},status = 200)
	elif request.method == 'POST':
		serializer = AutosSerializer(data = request.data)
		if serializer.is_valid():
			try:
				savedObject = create_vehiculos_process(serializer.data)

				return Response({'message' : 'rest fine'},status = 200)
			except Exception as e:
				return Response({'message' : 'error inserting the object in db', 'error' : str(e)})
		else:
			return Response({'message' : 'rest need params', 'data': serializer.errors},status = 200)
	else:
		return Response({'message' : 'method not suported'},status=405)


@api_view(['GET', 'POST'])
def list_vehiculos(request):
	if request.method == 'GET':
		return Response({'message' : 'api list vehiculo okey'},status = 200)
	elif request.method == 'POST':
		try:
			listObjects = list_vehiculos_process()
			
			return Response({'message' : 'rest fine','data':listObjects},status = 200)
		except Exception as e:
			return Response({'message' : 'error inserting the object in db', 'error' : str(e)})
	else:
		return Response({'message' : 'method not suported'},status=405)


def vehiculo_creation_form(request):
	if request.method == 'POST':
		form = VehiculoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = VehiculoForm()
	return render(request, 'core/creation.html', {
		'form': form
	})


def vehiculo_asossiation_form(request):
	if request.method == 'POST':
		form = Vehiculo_propietarioForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = Vehiculo_propietarioForm()
	return render(request, 'core/creation.html', {
		'form': form
	})


# MARCAS REST =======================================================================================================


@api_view(['GET', 'POST'])
def create_marcas(request):
	if request.method == 'GET':
		return Response({'message' : 'api add Marca okey'},status = 200)
	elif request.method == 'POST':
		serializer = MarcasSerializer(data = request.data)
		if serializer.is_valid():
			try:
				savedObject = create_marcas_process(serializer.data)

				return Response({'message' : 'rest fine'},status = 200)
			except Exception as e:
				return Response({'message' : 'error inserting the object in db', 'error' : str(e)})
		else:
			return Response({'message' : 'rest need params', 'data': serializer.errors},status = 200)
	else:
		return Response({'message' : 'method not suported'},status=405)


@api_view(['GET', 'POST'])
def list_marcas(request):
	if request.method == 'GET':
		return Response({'message' : 'api list Marca okey'},status = 200)
	elif request.method == 'POST':
		try:
			listObjects = list_marcas_process()
			
			return Response({'message' : 'rest fine','data':listObjects},status = 200)
		except Exception as e:
			return Response({'message' : 'error inserting the object in db', 'error' : str(e)})
	else:
		return Response({'message' : 'method not suported'},status=405)


def marca_creation_form(request):
	if request.method == 'POST':
		form = MarcaForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = MarcaForm()
	return render(request, 'core/creation.html', {
		'form': form
	})



# TIPOS REST =======================================================================================================


@api_view(['GET', 'POST'])
def create_tipos(request):
	if request.method == 'GET':
		return Response({'message' : 'api add Tipo okey'},status = 200)
	elif request.method == 'POST':
		serializer = TiposSerializer(data = request.data)
		if serializer.is_valid():
			try:
				savedObject = create_tipos_process(serializer.data)

				return Response({'message' : 'rest fine'},status = 200)
			except Exception as e:
				return Response({'message' : 'error inserting the object in db', 'error' : str(e)})
		else:
			return Response({'message' : 'rest need params', 'data': serializer.errors},status = 200)
	else:
		return Response({'message' : 'method not suported'},status=405)


@api_view(['GET', 'POST'])
def list_tipos(request):
	if request.method == 'GET':
		return Response({'message' : 'api list Tipo okey'},status = 200)
	elif request.method == 'POST':
		try:
			listObjects = list_tipos_process()
			
			return Response({'message' : 'rest fine','data':listObjects},status = 200)
		except Exception as e:
			return Response({'message' : 'error inserting the object in db', 'error' : str(e)})
	else:
		return Response({'message' : 'method not suported'},status=405)


def tipo_creation_form(request):
	if request.method == 'POST':
		form = TipoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = TipoForm()
	return render(request, 'core/creation.html', {
		'form': form
	})


# REPORTES REST ======================================================================================================


@api_view(['GET', 'POST'])
def vehiculosPorMarca(request):
	if request.method == 'GET':
		return Response({'message' : 'api list Tipo okey'},status = 200)
	elif request.method == 'POST':
		try:
			listObjects = report_marcas_process()
			
			return Response({'message' : 'rest fine','data':listObjects},status = 200)
		except Exception as e:
			return Response({'message' : 'error inserting the object in db', 'error' : str(e)})
	else:
		return Response({'message' : 'method not suported'},status=405)


@api_view(['GET', 'POST'])
def vehiculos_report(request):
	if request.method == 'GET':
		return Response({'message' : 'api list Tipo okey'},status = 200)
	elif request.method == 'POST':
		try:
			listObjects = report_vehiculos_process()
			
			return Response({'message' : 'rest fine','data':listObjects},status = 200)
		except Exception as e:
			return Response({'message' : 'error inserting the object in db', 'error' : str(e)})
	else:
		return Response({'message' : 'method not suported'},status=405)



def reporte_vehiculos_marca_view(request):
	
	return render(request, 'core/reporte_vehiculo_marca.html', {

	})



# FINDER REST ======================================================================================================

def finder_view(request):
	
	return render(request, 'core/finder.html', {

	})

@api_view(['GET', 'POST'])
def finder_rest(request):
	if request.method == 'GET':
		return Response({'message' : 'api list Tipo okey'},status = 200)
	elif request.method == 'POST':
		try:
			listObjects = finder(request.data)
			
			return Response({'message' : 'rest fine','data':listObjects},status = 200)
		except Exception as e:
			return Response({'message' : 'error inserting the object in db', 'error' : str(e)})
	else:
		return Response({'message' : 'method not suported'},status=405)