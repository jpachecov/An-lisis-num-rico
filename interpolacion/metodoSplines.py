#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Creado por Jean Pierre Pacheco Avila


from sympy import *
import numpy as np
import matplotlib.pyplot as plt


# funcion que devuelve la funcion de evaluacion asi como la expresion que representa
# al polinomio interolador de lagrange y tambien el simbolo de variable usado.


# n + 1 puntos
# splines cubicos	
def obtenSplineCubico(puntos,evaluaciones):
	vectorX = puntos
	vectorY = evaluaciones
	vectorHs = obtenHs(puntos)
	vectorb = obtenDiferencias(vectorHs,vectorY)

	vectorA = x = np.linalg.solve(creaTridiagonal(vectorHs),vectorb)
	
	vectorAs = np.zeros([len(puntos)])
	vectorAs[0] = 0
	for i in range(len(puntos) - 2):
		vectorAs[i+1] = vectorA[i]

	vectorAs[len(puntos) -1] = 0

	x = symbols('x')
	splines = []
	for i in range(len(puntos) - 1):
		f = (vectorAs[i]/(6*vectorHs[i]))*((vectorX[i+1] - x)**3) + (vectorAs[i+1]/(6*vectorHs[i]))*((x - vectorX[i])**3) + ((vectorY[i]/vectorHs[i])-(vectorAs[i]*vectorHs[i]/6))*(vectorX[i+1]-x) + ((vectorY[i+1]/vectorHs[i])-(vectorAs[i+1]*vectorHs[i]/6))*(x - vectorX[i])
		#(vectorAs[i]/6)*((((vectorX[i+1]-x)**3)/vectorHs[i])-vectorHs[i]*(vectorX[i+1]-x)) + (vectorAs[i+1])*((((x-vectorX[i])**3)/vectorHs[i])-vectorHs[i]*(x-vectorX[i])) + (vectorY[i])*((vectorX[i+1]-x)/vectorHs[i]) + (vectorY[i+1])*((x-vectorX[i])/vectorHs[i])
		print f
		splines.append(simplify(f))

	return lambda y : reglaDeCorrespondencia(x,y,splines,puntos)

def reglaDeCorrespondencia(simbolo,y,splines,puntos):
	if (y <= puntos[0]):
		return splines[0].subs(simbolo,y)

	if( y >= puntos[len(puntos)-1]):
		return splines[len(splines)-1].subs(simbolo,y)

	for i in range(len(splines)):
		if (puntos[i] <= y and y <= puntos[i+1]):
			return splines[i].subs(simbolo,y)



def obtenHs(x):
	h = np.zeros([len(x) - 1])
	for i in range(len(x)-1):
		h[i] = x[i+1] - x[i]
	return h


def obtenDiferencias(h,y):
	d = np.zeros([len(h)-1])

	for i in range(len(h)-1):
		d[i] = 6* (((y[i+2]- y[i+1])/(h[i+1])) - ((y[i+1]- y[i])/(h[i])))
	return d


def creaTridiagonal(h):
	A = np.zeros([len(h)-1,len(h)-1])

	for i in range(len(h)-1):
		A[i][i] = h[i] + h[i+1]
		if(i+1 != len(h)-1):
			A[i+1][i] = h[i+1]

	return A+A.T

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


def graficaPolinomio(f,puntos,amplitud):
	t2 = np.arange(puntos[0]-amplitud,puntos[len(puntos)-1]+amplitud,0.02)
	plt.plot(puntos, map(f,puntos), 'bo', t2, map(f,t2), 'k')
	plt.xlabel("X")
	plt.ylabel('S(X)')
	plt.title("SPLINE CUBICO.\n")
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

				f = obtenSplineCubico(X,Y)
				print "\n.El polinomio P ha sido calculado. Elige una opcion."
				sale = False;
				while(not sale):
					print "1. Grafica polinomio."
					print "2. Interpolar punto."
					print "3. Regresar al primer menu."
					print "4. Salir\n"
					try:
						opcion = int(raw_input("Elige una opcion: "))
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
							graficaPolinomio(f,X,5)

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

