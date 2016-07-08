#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Creado por Jean Pierre Pacheco Avila

from numpy import *
from random import randint
import sys

# Metodo que implementa el metodo de Jacobi
# A matriz de nxn
# b vector del sistema Ax = b
# X aproximacion inicial

def hazJacobi(A,b,X,iteraciones,epsilon):
	x_anterior = X
	n = size(A[0])
	x_nueva = zeros([n])
	num = 0
	while(num < iteraciones):
		for i  in range(0,n):
			suma = 0
			for j in range(0,n):
				if(j != i):
					suma += A[i][j]*x_anterior[j]

			x_nueva[i] = (1./A[i][i])*(b[i] - suma)

		if(linalg.norm(x_nueva - x_anterior,inf)/(linalg.norm(x_nueva,inf)) < epsilon):
			print "\nSe cumplió la tolerancia en la iteracion: ",num
			return x_nueva
		
		x_anterior = x_nueva.copy()
		num+=1
	print "Numero de iteraciones excedidas."
	return x_nueva



print "\nMETODO DE JACOBI.\n"
print "Se resolverá el sistema de ecuaciones Ax = b leyendo A y b de dos archivos de texto."

f = open("matriz.Res","r")

A = [map(float,line.split()) for line in f]

f = open("vectorB.Res","r")

b = [map(float,line.split()) for line in f]
B = [x for lista in b for x in lista]
f.close()

print "Matriz A:"
A = array(A)
print A
print "Vector b:"
print B
itera = 10000
epsilon = 0.000001
print "\nSolución con JACOBI: ","Maximas iteraciones: ",str(itera)," epsilon: ",str(epsilon)
print hazJacobi(A,B,[0]*len(B),itera,epsilon)
print "\nSolución con NUMPY: "
print linalg.solve(A,B)