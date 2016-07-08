#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Creado por Jean Pierre Pacheco Avila

import numpy as np
from pylab import *
import time

max_iter = 10000
epsilon = 0.000001

# Funcion que resuelve la ecuacion de laplace en 2D.
# nx - El tamaño de la placa en X
# ny - El tamaño de la placa en Y
# dx - Cambio en X
# dy - Cambio en Y
# arr,aba,izq y der - Valores iniciales.

def hazLaplace(nx,ny,dx,dy,aba,arr,izq,der,funcion):

	# Calculamos el numero de particiones en X y Y
	# Tambien coincide con el tama;o de la matriz con la
	# que vamos a trabajar.
	ren = int(nx/dx) + 1
	col = int(ny/dy) + 1
	U = np.zeros((ren,col),'d')

	
	# Llenamos las entradas de la matriz correspondientes
	# a los valores iniciales para las fronteras.

	U[0,:] = aba
	U[-1,:] = arr
	U[:,0] = izq
	U[:,-1] = der
	
	ecuaciones = []
	constantes = []
	
	i,j = 1,1
	while i < ren - 1:
		j = 1
		while j < col - 1:
			ec,cons = generaRenglon(U,i,j,(ren - 2),(col - 2))
			ecuaciones.append(ec)
			constantes.append(cons)
			j+=1
		i+=1 

	
	sistema = np.array(ecuaciones)
	constantes = np.array(constantes)
	solucion = funcion(sistema,constantes)
	print llenaMatriz(U,solucion,(ren - 2),(col - 2))
	return llenaMatriz(U,solucion,(ren - 2),(col - 2))

# Funcion para comparar tiempos de ejecucion al resolver un sistema de ecuaciones.
def comparaMetodos(sistema,constantes):
	T_inicio=time.time()
	solucion = hazJacobi(sistema,constantes,[0]*len(constantes),10000,0.1)
	T_fin=time.time()
	print "Tiempo de solución JACOBI: ", str(T_fin - T_inicio)

	T_inicio=time.time()
	solucion = np.linalg.solve(sistema,constantes)
	T_fin=time.time()
	print "Tiempo de solución NUMPY : ", str(T_fin - T_inicio)
	return solucion

# Funcion que usa la biblioteca numpy para resolver el sistema de ecuaciones 
# y verificar el tiempo que tarda
def usaNumpy(sistema,constantes):
	T_inicio=time.time()
	solucion = np.linalg.solve(sistema,constantes)
	T_fin=time.time()
	print "Tiempo de solución NUMPY : ", str(T_fin - T_inicio)
	return solucion

# Funcion que usa una implementacion propia de Jacobi para resolver el sistema
# y medir el tiempo que tarda.	
def usaJacobi(sistema,constantes):
	print "\n Si cambias a un epsilon mas pequeño tardará más pero el gráfico será mejor."
	T_inicio=time.time()
	solucion = hazJacobi(sistema,constantes,[0]*len(constantes),max_iter,epsilon)
	T_fin=time.time()
	print "Tiempo de solución JACOBI: ", str(T_fin - T_inicio)
	return solucion

# Dada la solucion y la matriz original U, llena las entradas faltantes de U con
# el vector solucion.
# n es el numero de renglones de la matriz 
# m es el numero de columnas

def llenaMatriz(U,sol,n,m):
	i,j = 1,1
	while i < np.shape(U)[0] - 1:
		j = 1
		while j < np.shape(U)[1] - 1:
			U[i,j] = sol[obtenIndice(i,j,m)]
			j+=1
		i+=1 
	return U

# Esta funcion genera un renglon de la matriz que debemos resolver.
# U, la matriz que necesitamos para construir el sistema de ecuaciones.
# i,j es la entrada de la matriz U que estamos procesando,
# n es el numero de renglones de la matriz
# m en el numero de columnas de la matriz
# Devuelve algo del estilo: [[-4,1,0,9,0,0,0,0,0],-5] que es equivalente a la siguiente ecuacion:
# -4a +b + 9d  = -5

def generaRenglon(U,i,j,n,m):

	# El metodo funciona de la siguiente manera:
	# Primero necesitamos numerar de alguna manera las variables que nos interesan,
	# y con las que estamos formando la matriz a resolver.
	# Para esto es el arreglo: vector.
	# Necesitamos una variable donde almacenar los valores constantes
	# que ya sabemos, esta variable es: constante.
	# si la posicion (i,j) está dentro de la submatriz de U, es decir,
	# tiene una posicion valida, entonces ésta entrada representa una variable
	# que aparece en la ecuacion correspondiente para U[i,j]
	# Si la posicion no es valida, quiere decir que el valor U[i,j] fue dado en 
	# las condiciones iniciales,(esta en el "marco", o en la "orilla", 
	# por asi decirlo, de la matriz U) y por tanto de suma a la variable constante.
	
	vector = [0]*(n*m)
	constante = 0.0
	
	indVar = obtenIndice(i,j,m)
	vector[indVar] = -4
	# derecha
	if(esPosicionValida(i,j+1,U)):
		indiceDer = obtenIndice(i,j+1,m)
		vector[indiceDer] = 1
	else:
		constante += -1*U[i,j+1]
	# arriba
	if(esPosicionValida(i-1,j,U)):
		indiceAr = obtenIndice(i-1,j,m)
		vector[indiceAr] = 1
	else:
		constante += -1*U[i-1,j]
	# izquierda
	if(esPosicionValida(i,j-1,U)):
		indiceIzq = obtenIndice(i,j-1,m)
		vector[indiceIzq] = 1
	else:
		constante += -1*U[i,j-1]
	# abajo
	if(esPosicionValida(i+1,j,U)):
		indAba = obtenIndice(i+1,j,m)
		vector[indAba] = 1

	else:
		constante += -1*U[i+1,j]
	return vector,constante


# Dada una posicion VALIDA (i,j), esta funcion devuelve el indice
# correspondiente a esta variable en un arreglo de tamaño n

def obtenIndice(i,j,n):
	return n*(i-1) + j - 1

# Verifica si (i,j) es una posicion valida en U, es decir,
# verifica si no está en el "marco" u "orilla" de U.(por asi decirlo)
# i - renglon
# j - columna
# U - Matriz
def esPosicionValida(i,j,U):
	# si i es el renglon cero o el ultimo renglon
	# o si j es la primer columna o la ultima columna de U
	if(i == 0 or i == len(U[:,0]) - 1 or  j == 0 or j == len(U[0]) - 1):
		return False
	return True


# Grafica la solucion dados todos los datos necesarios.
# nx Longitud de la placa en X.
# ny Longitud de la placa en Y
# dx Salto en la coordenada X.
# dy Salto en la coordenada Y.
# abajo, arriba, izq y der son las condiciones iniciales de frontera.

def graficaSolucion(nx,ny,dx,dy,abajo,arriba,izq,der,funcion):
	x = linspace(0,nx,int(nx/dx)+1)
	y = linspace(0,ny,int(ny/dy)+1)

	X,Y = meshgrid(x,y)
	print np.shape(X)
	print X
	# abajo,arriba, izq, der
	Z = hazLaplace(nx,ny,dx,dy,abajo,arriba,izq,der,funcion)
	
	"""""
	print np.shape(Z)
	fig, ax = plt.subplots()

	p = ax.pcolor(X, Y, Z, cmap=cm.hot, vmin=Z.min(), vmax=Z.max())
	cb = fig.colorbar(p, ax=ax)
	cb.ax.get_yaxis().labelpad = 15
	cb.ax.set_ylabel('temperaturas', rotation=270)
	plt.show()
	"""""
	fig = plt.figure(1) 
	plt.title('Contorno de Isotermas')
	plt.xlabel('Y')
	plt.ylabel('X')
	cs1 = plt.contourf(Z, 100) # Pintamos 100 niveles con relleno
	plt.colorbar()
	
	plt.show()

# Metodo que implementa el metodo de Jacobi
# A matriz de nxn
# b vector del sistema Ax = b
# X aproximacion inicial

def hazJacobi(A,b,X,iteraciones,epsilon):
	x_anterior = X
	n = np.size(A[0])
	x_nueva = np.zeros([n])
	num = 0
	while(num < iteraciones):
		for i  in range(0,n):
			suma = 0
			for j in range(0,n):
				if(j != i):
					suma += A[i][j]*x_anterior[j]

			x_nueva[i] = (1./A[i][i])*(b[i] - suma)
		
		if(np.linalg.norm(x_nueva - x_anterior,np.inf) / np.linalg.norm(x_nueva,np.inf) < epsilon):
			return x_nueva

		x_anterior = x_nueva.copy()
		num+=1

	return x_nueva


def menu():
	while(True):
		print "\nCALCULO DE TEMPERATURAS EN UNA PLACA"
		print "1. Dar datos para el problema."
		print "2. Salir."
		try:
			op = int(raw_input("Escribe una opcion: "))
		
			if(op == 2):
				print "El programa termina correctamente."
				return
			if(op == 1):
				nx = float(raw_input("Da el ancho de la placa: "))
				ny = float(raw_input("Da el alto de la placa : "))
				dx = float(raw_input("Da el tamaño del salto en X: "))
				dy = float(raw_input("Da el tamaño del salto en Y: "))
				izq = float(raw_input("Da la temperatura de la IZQUIERDA: "))
				der = float(raw_input("Da la temperatura de la DERECHA  : "))
				aba = float(raw_input("Da la temperatura de ABAJO       : "))
				arr = float(raw_input("Da la temperatura de ARRIBA      : "))


				while(True):
					print "\n1. Usar el método de numpy para resolver matriz."
					print "2. Usar Jacobi."
					print "3. Jacobi vs Numpy"
					print "4. Volver al menu anterior."
					try:
						op1 = int(raw_input("Escribe una opcion: "))
						ren = int(nx/dx) + 1
						col = int(ny/dy) + 1
						if(op1 == 1):
							print "\nSe resolverá una matriz de orden ",str((ren - 2)*(col - 2))," x ",str((ren - 2)*(col - 2))
							graficaSolucion(nx,ny,dx,dy,aba,arr,izq,der,usaNumpy)
						if(op1 == 2):
							print "\nSe resolverá una matriz de orden ",str((ren - 2)*(col - 2))," x ",str((ren - 2)*(col - 2))
							print "por lo que puede que Jacobi tarde demasiado..."
							print "Da dimensiones mas pequeñas al ancho, alto, o a los saltos."
							while(True):
								print "1. Esperar a que termine."
								print "2. Dar otras dimensiones."
								try:
									op3 = int(raw_input("Da una opcion: "))
									if(op3 == 1):
										print "\nPuedes detener la ejecucion de Jacobi aprentando ctrl+c o ctrl+d\n"
										print "Jacobi. maximas iteraciones: ",str(max_iter)," epsilon: ",str(epsilon)
										graficaSolucion(nx,ny,dx,dy,aba,arr,izq,der,usaJacobi)
										break
									if(op3 == 2):
										break
								except ValueError:
									print "Opcion invalida."
									continue
								except KeyboardInterrupt:
									print "\nLo siento, esta implementacion de Jacobi no es eficiente :("
									break
								except EOFError:
									print "\nLo siento, esta implementacion de Jacobi no es eficiente :("
									break

						if(op1 == 3):
							print "Se resolverá una matriz de orden ",str((ren - 2)*(col - 2))," x ",str((ren - 2)*(col - 2))
							print "por lo que puede que Jacobi tarde demasiado..."
							print "Se muestra grafico usando la solucion de numpy."
							graficaSolucion(nx,ny,dx,dy,aba,arr,izq,der,comparaMetodos)
						if(op1 == 4):
							break
					except ValueError:
						print "Opcion invalida, intenta de nuevo."
						continue
					except KeyboardInterrupt:
						print "\nOye!, no me puedes matar asi nadamás!"
						continue
					except EOFError:
						print "\nOye!, no me puedes matar asi nadamás!"
						continue

		except ValueError:
			print "Opción inválida, intenta de nuevo."
			continue
		except KeyboardInterrupt:
			print "\nOye!, no me puedes matar asi nadamás!"
			continue
		except EOFError:
			print "\nOye!, no me puedes matar asi nadamás!"
			continue
menu()