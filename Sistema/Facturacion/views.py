# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

# Templete Login
def login (request):
	return render(request,"Facturacion/login/login.html",{})
def restablecer (request):
    return render(request,"Facturacion/login/restablecer_login.html",{})


# Template base 
def base (request): 
    return render(request,"Facturacion/base.html",{}) 


#Templete de Clientes
def clientes (request): 
    return render(request,"Facturacion/administracion/Clientes/crear_clientes.html",{})  
def clientes_list (request): 
    return render(request,"Facturacion/administracion/Clientes/listar_clientes.html",{}) 


#Templete de Productos
def productos (request): 
    return render(request,"Facturacion/administracion/Productos/crear_productos.html",{})
def productos_list (request): 
    return render(request,"Facturacion/administracion/Productos/listar_productos.html",{})


#Templete de Administracion de Accesos/Usuarios   
def usuarios (request):
    return render(request,"Facturacion/administracion/Usuarios/usuarios.html", {})
def usuarios_list (request):
    return render(request,"Facturacion/administracion/Usuarios/listar_usuarios.html", {})


#Templete de Facturacion(Factura)   
def factura_venta (request): 
    return render(request,"Facturacion/administracion/Factura/factura_venta.html",{})  
def factura_list (request): 
    return render(request,"Facturacion/administracion/Factura/listar_factura.html",{})


#Templete de Creditos
def credito_list (request): 
    return render(request,"Facturacion/administracion/Creditos/listar_credito.html",{})


#Templete de Reportes
def reporte_venta (request): 
    return render(request,"Facturacion/administracion/Reportes/reportes_ventas.html",{})


#Templete de Configuración
def perfil_empresa (request): 
    return render(request,"Facturacion/administracion/Configuracion/perfil_de_la_empresa.html",{})
def perfil_usuario (request): 
    return render(request,"Facturacion/administracion/Configuracion/perfil_de_usuario.html",{})
def configuracion (request): 
    return render(request,"Facturacion/administracion/Configuracion/configuracion.html",{})


#Templete de Herramientas
def calendario (request): 
    return render(request,"Facturacion/administracion/Herramientas/calendario.html",{})
def calculadora (request): 
    return render(request,"Facturacion/administracion/Herramientas/calculadora.html",{})   
