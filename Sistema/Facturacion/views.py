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
    return render(request,"Facturacion/administracion/clientes.html",{})   

def productos (request): 
    return render(request,"Facturacion/administracion/productos.html",{})
    
def usuarios (request):
    return render(request,"Facturacion/administracion/usuarios.html", {})    

def factura_venta (request): 
    return render(request,"Facturacion/administracion/factura_venta.html",{})   
