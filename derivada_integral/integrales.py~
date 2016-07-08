#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ANALISIS NUMERICO 1
# Creado por Jean Pierre Pacheco Avila

import numpy as np
import sympy as sm

# No hay mucho que comentar, cada funcion implementa un metodo de integracion.

def integra_trapecio(f,a,b,h):
	puntos = np.arange(a,b,h)

	i = 1
	suma = 0
	while(i <= len(puntos) - 1):
		suma += f(puntos[i])
		i+=1
	return (h/2)*(f(a) + 2*suma + f(b))

def integra_simpson1(f,a,b,h):
	puntos = np.arange(a,b,h)

	i = 1
	suma1 = 0
	suma2 = 0
	while(i <= len(puntos) - 1):
		if(i % 2 != 0):
			suma1 += f(puntos[i])
		if(i % 2 == 0):
			suma2 += f(puntos[i])
		i+=1

	return (h/3)*(f(a) + 4*suma1 + 2*suma2 + f(b))

def integra_simpson3(f,a,b,h):
	puntos = np.arange(a,b,h)

	i = 1
	suma1 = 0
	suma2 = 0
	while(i <= len(puntos) - 2):
		suma1 += f(puntos[i]) + f(puntos[i + 1])

		i+=3
	i = 3
	while( i <= len(puntos) - 1):
		suma2 += f(puntos[i])
		i+=3

	return (3*h/8)*(f(a) + 3*suma1 + 2*suma2 + f(b))


# Obtiene el error relativo porcentual

def obtenERP(real,aprox):
	return np.abs((real - aprox)/aprox)*100


# COMIENZA INTERACCION


x = sm.symbols("x")
y = sm.symbols('y')
y = input("Escribe una función con variable x:")
a = (float)(raw_input("Dame el extremo izquierdo del intervalo a integrar : "))
b = (float)(raw_input("Dame el extremo derecho del intervalo a integrar : "))

f = lambda z: y.subs(x,z)

integral = sm.integrate(y, x)
print integral

real = integral.subs(x,b) - integral.subs(x,a)
trapecio = integra_trapecio(f,a,b,0.01)
simpson1 = integra_simpson1(f,a,b,0.01)
simpson3 = integra_simpson3(f,a,b,0.01)


print "f(x)  = ",y
print "Integral(f(x)) = ",integral
print "Integral de f en [",str(a),",",str(b),"]:"
print "Solucion exacta:    ",real
print "Regla Trapecio.     ",trapecio," ERP = ", obtenERP(real,trapecio)
print "Regla Simpson 1/3.  ",simpson1," ERP = ",obtenERP(real,simpson1)
print "Regla Simpson 3/8.  ",simpson3," ERP = ",obtenERP(real,simpson3)


