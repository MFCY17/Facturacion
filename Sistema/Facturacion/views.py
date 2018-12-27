# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def login (request):
	return render(request,"Facturacion/login/login.html",{})

def restablecer (request):
    return render(request,"Facturacion/login/restablecer_login.html",{})

def base (request): 
    return render(request,"Facturacion/base.html",{})  

def clientes (request): 
    return render(request,"Facturacion/administracion/crear_clientes.html",{})  

def clientes_list (request): 
    return render(request,"Facturacion/administracion/listar_clientes.html",{}) 

def productos (request): 
    return render(request,"Facturacion/administracion/crear_productos.html",{})

def productos_list (request): 
    return render(request,"Facturacion/administracion/listar_productos.html",{})
    
def usuarios (request):
    return render(request,"Facturacion/administracion/usuarios.html", {})     

def factura_venta (request): 
    return render(request,"Facturacion/administracion/factura_venta.html",{})  

def calendario (request): 
    return render(request,"Facturacion/administracion/calendario.html",{})

def calculadora (request): 
    return render(request,"Facturacion/administracion/calculadora.html",{})   
