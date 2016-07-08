#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from sympy import *

# Error requerido
EPSILON = 0.000001  # <-- por eso usamos %.6f como truncamiento

# Numero de iteraciones maximo
MAX_ITER = 50

# Para almacenar cada error
errores = []

# funcion para hacer biseccion
# a - punto inicial
# b - punto final
# n - numero de iteraciones
# f - funcion de evaluacion
#		del polinomio 

def hazBiseccion(a,b,n,f):
	
	# Decimos que la variable errores
	# es la declarada globalmente al
	# inicio del script

	global errores
	
	# Agregamos error

	errores.append("%.6f" % np.abs(b - a))

	# Verificamos condicion de paro

	if(n == 0):
		print "Se llego al limite de iteraciones, quede en el intervalo: "+"[" +str("%.6f" %a)+", "+str("%.6f" %b)+"]"
		return

	# Verificamos los extremos
	
	if(f(a) == 0):
		return a
	elif (f(b) == 0):
		return b
	
	# Los extremos tienen el mismo signo

	if(f(a)*f(b) > 0) :
		print "No se cumple el teorema del valor intermedio! i.e f("+str("%.6f" % a)+") * f("+str("%.6f" % b)+") < 0"
		return

	# Obtenemos el punto medio

	medio = (a + b)/2.

	# Verificamos condicion de paro
	
	if(f(medio) == 0 or np.absolute((b-a)) < EPSILON):
		print "encontre raiz = " + str("%.6f" % medio) 
		print "intervalo: ["+str("%.6f" % a)+" , "+str("%.6f" % b)+" ]"
		return medio

	# Tienen el mismo signo
	
	if(f(a)*f(medio) > 0):
		hazBiseccion(medio,b,n-1,f)

	# Tienen signo contrario
	
	if(f(a)*f(medio) < 0):
		hazBiseccion(a,medio,n-1,f)


def main():
	global errores
	print "\n\n Cálculo de raíces usando bisección \n\n" 
	
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

	
	if (a == b):
		print "Los extremos son los mismos!!"

	if(a <= b) :
		print "El intervalo inicial es:  [" +str(a)+" , "+str(b)+"]"
	else :
		print "El intervalo inicial es:  [" +str(b)+" , "+str(a)+"]"
	
	raiz = hazBiseccion(a,b,MAX_ITER,f)

	print "iteraciones = " + str(len(errores)) + "\n"
	print "iteracion     error "
	i = 0;
	while (i < len(errores)):
		print str(i + 1) + "          "+str(errores[i])
		i+=1
	

	# Generamos gráfico
	if(a != b):
		print "\n Se muestra la grafica entre los intervalos."
		p = plot(hx,(x, a, b), title=u"Gráfico",xlabel="x",ylabel="y", show=False)
		p[0].line_color = 'blue'
		p.show()
	else:
		print "\n Extremos iguales, se muestra la grafica en [-10,10] por default."
		p = plot(hx,(x, -10, 10),label="Hola", title=u"Gráfico",xlabel="x",ylabel="y", show=False)
		p[0].line_color = 'blue'
		p.show()

	

# especificamos que solo debe ejecutarse el main 
# y no todo el archivo como script
if __name__ == "__main__":
    main()