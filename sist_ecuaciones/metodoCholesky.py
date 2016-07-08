#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Creado por Jean Pierre Pacheco Avila

from numpy import *
from random import randint
import sys



# Checa si una matriz es definida positiva

def esDefinidaPositiva(A):
	n = range(1,size(A[0]) + 1)
	for i in n:
		if(linalg.det(A[0:i,0:i]) <= 0):
			return False
	return True


# Implenta el metodo de cholesky para resolucion de ecuaciones
# Ax = b

def hazCholesky(A,b):

	if(not esDefinidaPositiva(A)):
		print "LA MATRIZ NO ES DEFINIDA POSITIVA. NO PUEDE APLICARSE EL ALGORITMO."
		print A
		sys.exit()

	n = size(A[0])
	L = zeros([n,n])
	
	U = zeros([n,n])
	vecX = zeros([n])
	vecY = zeros([n])



	for i  in range(0,n):
		suma1 = 0
		for k in range(0,i):
			suma1 += (L[i][k])**2

		L[i][i] = (A[i][i] - suma1) ** (1/2.)

		for j in range(i+1,n):
			suma2 = 0
			for k in range(0,i):
				suma2 += (L[j][k])*(L[i][k])

			L[j][i] = (1/L[i][i])*(A[j][i] - suma2)

	U = L.T

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

print "\nMETODO DE CHOLESKY PARA MATRICES SIMETRICAS DEFINIDAS POSITIVAS.\n"
print "El programa generará una matriz simétrica de orden nxn.\n"
n = int(raw_input("Introduce las filas de la matriz cuadrada A: "))

matA = zeros([n,n])
vec = zeros([n])

for f in range(n):
	for c in range(f,n):
		matA[f][c] = randint(2, 9)


matA = matA + matA.T

for f in range (n):
	vec[f] = random.uniform(10, 15)

L,U,vecX,vecY = hazCholesky(matA,vec)

print "Matriz A: \n",matA
print "Matriz L: \n",L
print "Matriz L*: \n",U
print "Vector b: ",vec
print "Vector Y: ",vecY
print "Vector X: ",vecX

x = linalg.solve(matA,vec) 
print "\nSolucion numpy: ",x


