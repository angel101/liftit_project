from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('health', views.health, name='health'),
	path('create_propietario', views.create_propietatios, name='create propietatios'),
	path('list_propietario', views.list_propietatios, name='list propietatios'),
	path('create_vehiculo', views.create_vehiculos, name='create vehiculos'),
	path('list_vehiculo', views.list_vehiculos, name='list vehiculos'),
	path('create_marca', views.create_marcas, name='create marcas'),
	path('list_marca', views.list_marcas, name='list marcas'),
	path('create_tipo', views.create_tipos, name='create tipos'),
	path('list_tipo', views.list_tipos, name='list tipos'),
	path('crear_propietatio_view', views.user_creation_form_upload, name = 'crear propietatio'),
	path('marca_creation_view', views.marca_creation_form, name = 'crear marca'),
	path('tipo_creation_view', views.tipo_creation_form, name = 'crear tipo'),
	path('vehiculo_creation_view', views.vehiculo_creation_form, name = 'vehiculo tipo'),
	path('vehiculo_asossiation_view', views.vehiculo_asossiation_form, name = 'vehiculo assossiation'),
]