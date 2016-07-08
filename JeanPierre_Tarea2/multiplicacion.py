# Programa para ejemplificar las operaciones
# con matrices usando python.

# autor: Jean Pierre Pacheco Avila

import numpy as np
import sys
import random as rand

# Obtiene la n-esima columna de una matriz.
# Tomo en cuenta una matriz en python (numpy)
# es una lista de vectores (renglones)
def columna(n, matriz):
	columna = []
	for x in matriz:
		columna.append(x[n])
	return columna;



# Comienza bucle para interaccion con el usuario
# para evitar errores el usuario da
# las dimensiones de la primera matriz A (mxn) y el numero
# de columnas de la segunda B (k), y el programa
# devuelve R = A*B  de dimension mxk

print ("\n======MULTIPLICACION DE MATRICES======\n")

while(True) :
	
	print ("1. Dar las dimensiones de las matrices.")
	print ("2. Salir.\n")

	# Leemos la opcion que da el usuario

	try:
		opcion = int(input())			
	
	# Manejo de errores
	except ValueError:
		print ("\n\nEsa opcion no es valida!")
		print ("intenta de nuevo...\n\n")
		continue
	
	if(opcion == 1):
		print ("\nEscribe las dimensiones de A: ")
		print ("renglones = ")
		try:
			renglones = int(input())			
		except ValueError:
			print ("\n\nEsa opcion no es valida!")
			print ("intenta de nuevo...\n\n")
			continue
		print ("renglones = ", renglones)
		print ("columnas = ")
		try:
			columnas = int(input())			
		except ValueError:
			print ("\n\nEsa opcion no es valida!")
			print ("intenta de nuevo...\n\n")
			continue
		
		print("Escribe las columnas de B: ")

		columnasB = int(input())

		# Creamos matrices de las dimensiones dadas
		# inicializadas en cero

		matrizA = np.zeros([renglones,columnas])
		matrizB = np.zeros([columnas,columnasB])
		matrizR = np.zeros([renglones,columnasB])


		# Lleanamos la matriz A 
		# con valores flotantes aleatorios en el
		# intervalo (0,5).
		
		for r in range(renglones):
			for s in range(columnas):
				matrizA[r][s] = rand.uniform(0,5)

		# Lleanamos la matriz B 
		# con valores flotantes aleatorios en el
		# intervalo (0,5).
		
		for r in range(columnas):
			for s in range(columnasB):
				matrizB[r][s] = rand.uniform(0,5)


		# A[i] devuelve el i-esimo renglon de A
		# Generamos la mtriz resultado pero por columnas
		# es decir, primero llenamos las columnas
		# de la matriz reultante.

		for r in range(columnasB):
			for s in range(renglones):

				# Obtenemos el vector resultado de
				# la multiplicacion componente a componente
				# de un renglon de A con una columna de B
				# usando funciones lambda.

				vector = map(lambda x,y: x*y,matrizA[s],columna(r,matrizB))
				suma = 0
				for x in vector:
					suma+=x

				matrizR[s][r] +=  suma

		# Imprimimos los resultados

		print ("\n\nMatriz A: \n")
		print matrizA
		print ("\n\nMatriz B: \n")
		print matrizB
		print ("\n\nMatriz resultado de AB:")
		print (matrizR)
		print ("\n\nUsando NUMPY:\n")
		print (np.dot(matrizA,matrizB))
		print ("\n\n")

		print ("continuar: (s/n)")
		x = raw_input()
		if(x == "s" or x == "S") :
			continue
		elif (x == "n" or x == "N"):
			break

	# Se termina bucle principal
	elif (opcion == 2):
		break;

	# La opcion es un entero pero no es ninguna
	# opcion valida

	print("\n\nNo existe esa opcion.\n\n")

