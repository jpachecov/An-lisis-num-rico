#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ANALISIS NUMERICO 1
# Creado por Jean Pierre Pacheco Avila


import numpy as np
import sympy as sm

# No hay mucho que comentar, cada funcion implementa un metodo de derivacion.

def primera_progresiva(f,xi,delta):
	return (f(xi + delta) - f(xi))/delta

def primera_regresiva(f,xi,delta):
	return (f(xi) - f(xi - delta))/delta

def primera_central(f,xi,delta):
	return (f(xi + delta) - f(xi - delta))/(2*delta)	



def segunda_progresiva(f,xi,delta):
	return (f(xi + 2*delta) - 2*f(xi + delta) + f(xi))/(delta**2)

def segunda_regresiva(f,xi,delta):
	return (f(xi) - 2*f(xi - delta)+ f(xi - 2*delta))/(delta**2)

def segunda_central(f,xi,delta):
	return (f(xi - delta) -2*f(xi) + f(xi + delta))/(delta**2)	



# Obtiene el error relativo porcentual

def obtenERP(real,aprox):
	return np.abs((real - aprox)/aprox)*100

# COMIENZA INTERACCION

x = sm.symbols("x")
y = sm.symbols('y')
y = input("Escribe una función con variable x:")
n = (float)(raw_input("Dame el punto donde quieres evaluar la primera y segunda derivada:"))
f = lambda z: y.subs(x,z)

derivada = sm.diff(y, x)
real = derivada.subs(x,n)
progre1 = primera_progresiva(f,n,0.01)
regre1 = primera_regresiva(f,n,0.01)
central1 = primera_central(f,n,0.01)

print "f(x)  = ",y
print "f'(x) = ",derivada
print "PRIMERA DERIVADA"
print "Solucion exacta. f'(",str(n),") = ",	real
print "Progresiva.      f'(",str(n),") = ",progre1," ERP = ", obtenERP(real,progre1)
print "Regresiva.       f'(",str(n),") = ",regre1," ERP = ",obtenERP(real,regre1)
print "Central.         f'(",str(n),") = ",central1," ERP = ",obtenERP(real,central1)


progre2 = segunda_progresiva(f,n,0.01)
regre2 = segunda_regresiva(f,n,0.01)
central2 = segunda_central(f,n,0.01)
segunda_de = sm.diff(derivada,x)
real2 = segunda_de.subs(x,n)
print "SEGUNDA DERIVADA"
print "Solución exacta. f''(",str(n),") = ",real2
print "Progresiva.      f''(",str(n),") = ",progre2," ERP = ", obtenERP(real2,progre2)
print "Regresiva.       f''(",str(n),") = ",regre2," ERP = ", obtenERP(real2,regre2)
print "Central.         f''(",str(n),") = ",central2," ERP = ", obtenERP(real2,central2)





