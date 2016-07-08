#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Creado por Jean Pierre Pacheco Avila


from sympy import *
import numpy as np
import matplotlib.pyplot as plt


# funcion que devuelve la funcion de evaluacion asi como la expresion que representa
# al polinomio interolador de lagrange y tambien el simbolo de variable usado.

def obtenPolinomioLagrange(puntos,evaluaciones):
	x = symbols('x')
	exp = 0
	sumandos = map(lambda L,F: L*F,construyeLs(puntos,x),evaluaciones)
	for sumando in sumandos:
		exp += sumando
	exp = simplify(exp)
	return lambdify(x,exp,"numpy"),exp,x


# Funcion que devuelve una lista con n polinomios de lagrange
# donde n es el numero de puntos
# x es un objeto de tipo symbols, necesario para crear una expresion de sympy.

def construyeLs(puntos,x):
	polinomiosL = []

	for p in puntos:
		numerador = 1
		denominador = 1
		
		for q in puntos:
			if(q != p):
				numerador *= x - q
				denominador *= p - q
		polinomiosL.append(numerador/denominador)
	
	return polinomiosL


def graficaPolinomio(exp,f,x,puntos,amplitud):
	t2 = np.arange(puntos[0]-amplitud,puntos[len(puntos)-1]+amplitud,0.02)
	plt.plot(puntos, map(f,puntos), 'bo', t2, f(t2), 'k')
	plt.xlabel("X")
	plt.ylabel('P(X)')
	plt.title("POLINOMIO INTERPOLADOR DE LAGRANGE.\n"+str(exp))
	plt.grid(True)
	plt.show()



def main():
	salida = 1

	while(salida):
		print("METODO DE INTERPOLACION DE LAGRANGE.")
		print("1. Dar puntos y sus evaluaciones para encontrar polinomio.")
		print("2. Salir")

		try:
			opcion = int(raw_input())			
		except ValueError:
			print "\n\nEsa opcion no es valida!"
			print "intenta de nuevo...\n\n"
			continue

		# Mostramos la solucion al problema especifico
		if(opcion == 1):
			try:
				print "\nDa los puntos X separados por espacio:"
				print "Por ejemplo: X = 2 12 -2 35.5 63"
				punts = raw_input("X = ")
				X = map(float,punts.split())
				print "\nDa los puntos Y separados por espacio:"
				print "Por ejemplo: Y = 2 12 -2 35.5 63"
				punts = raw_input("Y = ")
				Y = map(float,punts.split())
				if(len(X) != len(Y)):
					raise ValueError

				f,exp,x = obtenPolinomioLagrange(X,Y)
				print "\n.El polinomio P ha sido calculado. Elige una opcion."
				sale = False;
				while(not sale):
					print "1. Grafica polinomio."
					print "2. Interpolar punto."
					print "3. Regresar al primer menu."
					print "4. Salir\n"
					try:
						opcion = int(raw_input())
						if(opcion == 4):
							return
						if(opcion == 3):
							sale = True
						if(opcion == 2):
							try:
								punto = float(raw_input("Dame el punto: "))
								print "\nP(",str(punto),") = ",f(punto),"\n"

							except ValueError:
								print "hubo error."
								continue
						if(opcion == 1):
							graficaPolinomio(exp,f,x,X,5)

					except ValueError:
						print "\n\nEsa opcion no es valida!"
						print "intenta de nuevo...\n\n"
						continue			

			except ValueError:
				print "Alguno no es numero! o los tamaños difieren!"
				continue

		# Leemos lista y calculamos lo debido
		if(opcion == 2):
			salida = 0

# especificamos que solo debe ejecutarse el main 
# y no todo el archivo como script

if __name__ == "__main__":
    main()

