"""Sistema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Facturacion import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #Login
    url(r'^$', views.login, name='login'),
    url(r'^restablecer/', views.restablecer, name='restablecer'),

    #Base 
    url(r'^administracion/', views.base, name='base'),

    #Clientes
    url(r'^crear_clientes/', views.clientes, name='clientes'),
    url(r'^listar_clientes/', views.clientes_list, name='clientes_list'),

    #Productos
    url(r'^crear_productos/', views.productos, name='productos'),
    url(r'^listar_productos/', views.productos_list, name='productos_list'),

    #Administracion de accesos(Usuarios)
    url(r'^crear_usuarios/', views.usuarios, name='usuarios'),
    url(r'^listar_usuarios/', views.usuarios_list, name='usuarios_list'),

    #Facturacion
    url(r'^nueva_venta/', views.factura_venta, name='factura_venta'),
    url(r'^listar_factura/', views.factura_list, name='factura_list'),

    #Creditos
    url(r'^listar_credito/', views.credito_list, name='credito_list'),

    #Reportes
    url(r'^reportes_ventas/', views.reporte_venta, name='reporte_venta'),

    #Configuracion
    url(r'^perfil_empresa/', views.perfil_empresa, name='perfil_empresa'),
    url(r'^perfil_usuario/', views.perfil_usuario, name='perfil_usuario'),
    url(r'^configuracion/', views.configuracion, name='configuracion'),

    #Herramientas
    url(r'^calendario/', views.calendario, name='calendario'),
    url(r'^calculadora/', views.calculadora, name='calculadora'),




]
