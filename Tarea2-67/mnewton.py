#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Analisis numerico 1. prgrama para calcular raices usando el metodo de Newton-Raphson
# Hecho por Jean Pierre Pacheco Avila

import numpy as np
from sympy import *

# Error requerido
EPSILON = 0.000001  

# Numero de iteraciones maximo
MAX_ITER = 50

# Para almacenar cada error
errores = []

# Para almacenar las aproximaciones
aprox = []

# Guardamos el numero de digitos de precision requerida

DIGITOS =  (str(EPSILON))[len(str(EPSILON)) - 1]

# funcion recursiva para aproximar raices 
# usando el metodo de Newton-Raphson.
# p aproximacion a la raiz
# n - numero de iteraciones
# f - funcion de evaluacion de la funcion
# df - funcion de evaluacion de la derivada de f

def NewtonRaphson(f,df,p,n):

	# Usamos variables globales

	global errores
	global MAX_ITER
	global intervalos
	global DIGITOS

	# para hacer truncamiento

	tru = "%." +DIGITOS+"f" 

	# Verificamos condicion de paro

	if(n == 0):
		raise Exception("Se llego al limite de iteraciones el punto final calculado es p = " + str(p))
	

	# Obtenemos la aproximacion

	raiz_aprox =  p - (f(p)/df(p))
	aprox.append(raiz_aprox)
	errores.append(np.absolute((raiz_aprox - p)/raiz_aprox))

	# Vemos si encontramos raiz

	if(f(raiz_aprox) == 0):
		print "Encontre raiz = "+str(tru % raiz_aprox)
		return raiz_aprox

	
	
	# Verificamos condicion de paro
		
	if(np.absolute((raiz_aprox) - p)/np.absolute(raiz_aprox) < EPSILON):
		print "encontre raiz = " + str(raiz_aprox) 
		return raiz_aprox


	NewtonRaphson(f,df,raiz_aprox,n-1)


# main

def main():
	global errores
	print "\n\n Cálculo de raíces usando el metodo de Newton-Rapson. \n\n" 
	
	# Leeemos funcion de variable x

	x = Symbol('x')
	
	# hx es nuestra funcion de varibale x
	hx = input("Introduce una funcion donde x es la variable independiente: ")

	# Funcion para evluar una expresion (funcion) 

	g = lambda f,y: f.evalf(subs={x:y})


	# Funcion para evaluar la funcion
	# usada por el metodo de newton

	f = lambda z: g(hx,z)
	
	# obtenemos expresion de la funcion derivada de hx

	derivada = diff(hx,x)
	
	# obtenemos la funcion de evaluacion de 
	# la derivada de hx, necesaria para el metodo.

	df = lambda x: g(derivada,x)

	print "\nf(x) =  " + str(hx)
	print "f'(x) = " + str(derivada)

	# Obtenemos punto inicial

	print "\nProporciona un punto inicial p0."
	p0 = float(raw_input("p0 = "))

	# Generamos gráfico

	print "\n Se muestra la grafica en [-10,10]"
	p = plot(hx,(x, -10, 10),label="Hola", title=u"Gráfico",xlabel="x",ylabel="y", show=False)
	p[0].line_color = 'blue'
	p.show()

	try:

		raiz = NewtonRaphson(f,df,p0,MAX_ITER)

	except Exception as e:
	
		mensaje = e.args
		print mensaje

		print "El programa termina."
		return

	print "iteraciones = " + str(len(errores)) + "\n"
	print "iteracion     aproximacion      error "
	i = 0;
	while (i < len(errores)):
		print str(i + 1) +"          "+str(aprox[i])+"          "+str(errores[i])
		i+=1

	

# especificamos que solo debe ejecutarse el main 
# y no todo el archivo como script

if __name__ == "__main__":
    main()