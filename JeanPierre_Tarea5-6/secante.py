#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Analisis numerico 1. Tarea 5. Metodo de la secante para aproximacion de raices.
# Hecho por Jean Pierre Pacheco Avila


import numpy as np
from sympy import *

# Error requerido
EPSILON = 0.000000001  

# Numero de iteraciones maximo
MAX_ITER = 50

# Para almacenar cada error
errores = []

# Guardamos el numero de digitos de precision requerida

DIGITOS =  (str(EPSILON))[len(str(EPSILON)) - 1]

# funcion recursiva para aproximar raices 
# usando el metodo de la secante.
# a - punto inicial
# b - punto final
# n - numero de iteraciones
# f - funcion de evakuacion de la funcion

def secante(a,b,n,f):

	# Usamos variables globales

	global errores
	global MAX_ITER
	global intervalos
	global DIGITOS

	# para hacer truncamiento

	tru = "%." +DIGITOS+"f" 

	# Verificamos condicion de paro

	if(n == 0):
		raise Exception("Se llego al limite de iteraciones, quede en el intervalo: "+"[" +str(tru%a)+", "+str(tru%b)+"]")
	
	# Obtenemos la aproximacion

	raiz_aprox =   b - f(b)*((b - a)/(f(b) - f(a)) ) #(a*f(b) - b*f(a)) / (f(b) - f(a))
	
	errores.append(tru%f(raiz_aprox))
	
	# Verificamos condicion de paro
		
	if(np.absolute(f(raiz_aprox)) < EPSILON or np.absolute((raiz_aprox-b)) < EPSILON):
		print "encontre raiz = " + str(tru % raiz_aprox) 
		print "intervalo: ["+str(tru % a)+" , "+str(tru % b)+" ]"
		return raiz_aprox


	secante(b,raiz_aprox,n-1,f)


# main

def main():
	global errores
	print "\n\n Cálculo de raíces usando el metodo de la secante. \n\n" 
	
	# Leeemos polinomio
	x = Symbol('x')
	hx = input("Introduce una funcion donde x es la variable independiente: ")

	# Funcion para evluar una expresion 

	g = lambda f,y: f.evalf(subs={x:y})

	# Funcion para evaluar el polinomio
	# usada por el metodo de biseccion.

	f = lambda z: g(hx,z)
	
	# Obtenemos intervalo
	print "Proporciona un intervalo [a,b]."
	a = float(raw_input("a = "))      
	b = float(raw_input("b = ")) 

		# Generamos gráfico
	if(a != b):
		print "\n Se muestra la grafica entre los intervalos."
		p = plot(hx,(x, a, b), title=u"Gráfico",xlabel="x",ylabel="y", show=False)
		p[0].line_color = 'blue'
		p.show()

	if (a == b):
		print "\n Extremos iguales, se muestra la grafica en [-10,10] por default."
		p = plot(hx,(x, -10, 10),label="Hola", title=u"Gráfico",xlabel="x",ylabel="y", show=False)
		p[0].line_color = 'blue'
		p.show()

	if(a <= b) :
		print "El intervalo inicial es:  [" +str(a)+" , "+str(b)+"]"
	else :
		print "El intervalo inicial es:  [" +str(b)+" , "+str(a)+"]"
	
	try:

		raiz = secante(a,b,MAX_ITER,f)

	except Exception as e:
	
		mensaje = e.args
		print mensaje

		print "El programa termina."
		return

	print "iteraciones = " + str(len(errores)) + "\n"
	print "iteracion     error "
	i = 0;
	while (i < len(errores)):
		print str(i + 1) +"         "+str(errores[i])
		i+=1

	

# especificamos que solo debe ejecutarse el main 
# y no todo el archivo como script

if __name__ == "__main__":
    main()

def maximo(lista):

	max = lista[0]
	for elemento in lista:
		if elemento > max:
			max = elemento
	return max
