#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Analisis numerico 1. Programa para encontrar raices usando el metodo de punto fijo
# Hecho por Jean Pierre Pacheco Avila

import numpy as np
from sympy import *

# Error requerido
EPSILON = 0.000000001  

# Numero de iteraciones maximo
MAX_ITER = 50

# Para almacenar cada error
errores = []

# Para almacenar las aproximaciones
aprox = []


# funcion recursiva para calcular raices usando el metodo de punto fijo
# f la funcion original
# g, de la forma g(x) = x, en esta implementacion use g(x) = x - f(x)/f'(x)
# p, aproximacion a la raiz
# n- numero de iteraciones

def puntofijo(f,g,p,n):
	if(n == 0):
		print "Se llego al limite de iteraciones, la ultima aproximacion es " + str(p)
		return

	nuevo = g(p)

	aprox.append(nuevo)
	errores.append(np.absolute(nuevo - p))

	if (np.absolute(nuevo - p) < EPSILON):
		print "Encontre la raiz p = "+ str(nuevo)
		return nuevo

	puntofijo(f,g,nuevo,n-1)

# main()
def main():
	global errores
	print "\n\n Cálculo de raíces usando el método de punto fijo\n\n" 
	
	# Leeemos funcion
	x = Symbol('x')
	fx = input("Introduce una funcion donde x es la variable independiente: ")

	# Funcion para evluar una expresion 

	evalua = lambda f,y: f.evalf(subs={x:y})


	# funcion de evaluacion de f(x)
	f = lambda x: evalua(fx,x)
	
	# Funcion para evaluar la funcion g(x) = x - f(x)/f'(x)
	# usada por el metodo de punto fijo

	g = lambda z: evalua(x - fx/diff(fx,x),z)
	
	derivada = diff(x - fx/diff(fx,x),x)

	# funcion de evaluacion de g'(x)

	dg = lambda x: evalua(derivada,x)


	print "dame un punto inicial p0 "
	p0 = float(raw_input("p0 = "))
	
	while(np.absolute(dg(p0)) >= 1):
		print "No se cumplen las condiciones para aplicar el metodo, da p0: "
		p0 = float(raw_input("p0 = "))


	# Generamos gráfico

	print "\n Se muestra la grafica en [-10,10]"
	p = plot(fx,(x, -10, 10),label="Hola", title=u"Gráfico",xlabel="x",ylabel="y", show=False)
	p[0].line_color = 'blue'
	p.show()

	raiz = puntofijo(f,g,p0,MAX_ITER)

	print "iteraciones = " + str(len(errores)) + "\n"
	print "iteracion     aproximacion    error "
	i = 0;
	while (i < len(errores)):
		print str(i + 1) + "          "+ str(aprox[i])+"        "+str(errores[i])
		i+=1
	

# especificamos que solo debe ejecutarse el main 
# y no todo el archivo como script
if __name__ == "__main__":
    main()