#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Creado por Jean Pierre Pacheco Avila bansandose fuertemente en el codigo
# porporcionado por Benjamin.

from numpy import *
from random import randint
import sys



def hazLU(A,b):

	n = size(A[0])
	L = zeros([n,n])
	U = zeros([n,n])
	vecX = zeros([n])
	vecY = zeros([n])


	L[0][0] = A[0][0]
	U[0][0] = 1.0


	# Verificamos que pueda aplicarse el método

	if (L[0][0] * U[0][0] == 0):

		print "EL programa se indetermina y se cerrará..."
		sys.exit(1)

	for j in xrange(1,n):

		U[0][j] = A[0][j] / L[0][0]
		L[j][0] = A[j][0]

	for i in range(1,n):

		U[i][i] = 1.

		for j in range(i,n):

			sumaU = 0
			sumaL = 0

			for k in range(i):

				sumaL = sumaL + L[j][k] * U[k][i]

			L[j][i] = (1 / U[i][i]) * ( A[j][i] - sumaL)

			for k in range(i):
				
				sumaU = sumaU + L[i][k] * U[k][j]

			U[i][j] = (1 / L[i][i]) * (A[i][j]-sumaU)


		if (L[i][i] * U[i][i] == 0):
			print "EL programa se indetermina y se cerrará..."
			sys.exit(1)

	# Encontramos el vector Y

	vecY[0] = b[0] / L[0][0]
	
	for i in range(1,n):
		sumaY = 0
		for j in range(i):
			sumaY = sumaY + L[i][j] * vecY[j]
		vecY[i] = (1/L[i][i]) * (b[i]-sumaY)

	# Encontramos el vector X

	vecX[n-1] = vecY[n-1] / U[n-1][n-1]
	
	for i in range(n-1,-1,-1):
		sumaX = 0
		for j in range(i+1,n):
			sumaX = sumaX + U[i][j]*vecX[j]
		vecX[i] = (1/U[i][i]) * (vecY[i]-sumaX)

	return L,U,vecX,vecY	

#.......Generar Aleatoriamente Matrices y vector solución (1)............#

n = int(raw_input("Introduce las filas de la matriz cuadrada A: "))

matA = zeros([n,n])
vec = zeros([n])

for f in range (n):
	for c in range(n):
		matA[f][c] = randint(2, 9)

for f in range (n):
	vec[f] = random.uniform(10, 15)
	
L,U,vecX,vecY = hazLU(matA,vec)

print "Matriz A: \n",matA
print "Matriz L: \n",L
print "Matriz U: \n",U
print "Vector b: ",vec
print "Vector Y: ",vecY
print "Vector X: ",vecX

x = linalg.solve(matA,vec) 
print "Solucion numpy: ",x


