#! /usr/bin/env python
# -*- coding: utf-8 -*-
import math


# Tarea 1. Análisis numérico. Prof: Roberto Rosas Espinosa
# Código elaborado por Jean Pierre Pacheco Avila
# Este codigo es libre y puede usarse de cualquier forma.



# Convierte un numero decimal
# a su representacion en la base dada

def dectother(decimal, base):

	# si la base sale del rango terminamos
	if base < 2 or base > 16:
		return

	simbolos = "0123456789ABCDEF"
	numero = []
	while(decimal != 0):
		r = decimal % base
		numero.append(simbolos[r])
		decimal/=base

	i = len(numero) -1
	nuevo = ""
	while i >=	 0:
		nuevo+=numero[i]
		i+=-1
	return nuevo


# Convierte un numero original y en cierta base, a su
# representacion en base decimal

def basetodec(original, base):

	if base < 2 or base > 16:
		return
	if base == 10:
		return int(original)
	max_pot = len(original) - 1
	numero = 0
	for y in original:
		numero += int(y) * (base**max_pot)
		max_pot+=-1
	return numero


# Funcion que obtiene el epsilon maquina
# de una palabra doble

def epsilonM():
	epsilon = 0
	x = 1.
	while x != 0:
		x /= 2
		if x != 0 :
			epsilon = x
	return epsilon


# Funcion para aproximar a la funcion exponencial
# usando series de Taylor, sumando los primeros n terminos.
# El criterio de paro para esta funcion es solamente terminar de sumar
# lo n primeros terminos de la serie, aunque podriamos usar la formula del error
# para poder dar una aproximacion con un error menor a "cualquier" epsilon dado.

def myexp(x,n):
	if  n < 1:
		print "No puedes aproximar con 0 o menos terminos"
		return

	if x < 0:
		return 1./myexp(-x,n)

	suma = 0
	i = 0

	# calculamos suma
	while i < n:
		suma+= (x**i + 0.)/ math.factorial(i)
		i+=1
	return suma


# Funcion para aproximar a la funcion coseno
# usando la serie de Maclaurin sumando los primeros n terminos

def cos_aprox(x,n):
	
	# usamos el hecho de que cos(x) es 2pi periodica
	# asi que si x no esta en [0,2pi] usamos el modulo

	if x < 0 or x > 2*math.pi:
		x = x%(2*math.pi)

	if n < 1:
		return
	suma = 0
	i = 0

	# Calculamos suma
	while i < n:
		suma+= ( (x**(2*i))*((-1)**i) )/ math.factorial(2*i)
		i+=1
	return suma


# Calcula el error relativo porcentual usando 8 digitos de aproximacion

def calcula_error(original, aproximacion):
	if(aproximacion == 0):
		return
	return "%.8f" % (100*(math.fabs(original - aproximacion)/aproximacion))


# Loop principal

def main():

	while 1 :
		print "\nTarea 1. Análisis numérico.\n"
		print "1. Convertir numeros entre bases."
		print "2. Encontrar epsilon maquina de este equipo."
		print "3. Aproximar exp(x) usando series de Taylor."
		print "4. Aproximar cos(x) usando la serie de Maclaurin."
		print "5. Calcular errores para la aproximacion de cos(x)"
		print "6. Salir\n"

		bien = False
		while not(bien):
			try:
				opcion = (int)(raw_input("\nTecla una opcion y oprime enter:  "))
			except ValueError:
				print "Esa no es una opcion valida"
				continue
			bien = True

		# Convertir numeros de una base a otra
		# se hace usando las 2 funciones definidas
		# primero transformamos el numero original a decimal
		# y despues ese numero decimal al  numero en la nueva base.

		if opcion == 1:
			numero = raw_input("\nnumero original: ")
			base = (int)(raw_input("base orignal: "))
			basen = (int)(raw_input("base nueva: "))
			decimal = basetodec(numero,base)
			nuevo = dectother(decimal,basen)
			print "Conversion:  "+ numero + "("+str(base)+") = "+str(nuevo) + "("+str(basen)+")\n"

		# Obtenemos epsilon maquina

		elif opcion == 2:
			print "\n epsilon maquina = " + str(epsilonM())
		
		# Apromimacion a exp(x)

		elif opcion == 3:
			try:
				x = (float)(raw_input("\n x =  "))
			except ValueError:
				print "Debe ser un real"
				continue

			try:
				terminos = (int)(raw_input("\nCon cuántos terminos de la serie quieres aproximar:  "))
			except ValueError:
				print "Debe ser un natural"
				continue


			print "\nPython dice: "+ "exp("+str(x) + ") = " + str(math.exp(x))
			print "Serie  dice: "+ "exp("+str(x) + ") = " + str(myexp(x,terminos))

		# Aproximacion de cos(x)

		elif opcion == 4:
			try:
				x = (float)(raw_input("\n x =  "))
			except ValueError:
				print "Debe ser un real"
				continue

			try:
				terminos = (int)(raw_input("\nCon cuántos terminos de la serie quieres aproximar:  "))
			except ValueError:
				print "Debe ser un natural"
				continue


			print "\nPython dice: "+ "cos("+str(x) + ") = " + str(math.cos(x))
			print "Serie  dice: "+ "cos("+str(x) + ") = " + str(cos_aprox(x,terminos))
		
		# Calculo de errores relativos absolutos para cos(x)

		elif opcion == 5:
			try:
				x = (float)(raw_input("\n x =  "))
			except ValueError:
				print "Debe ser un real"
				continue

			try:
				terminos = (int)(raw_input("\nCon cuántos terminos de la serie quieres calcular el error:  "))

			except ValueError:
				print "Debe ser un natural"
				continue
			i = 1
			print "x = "+str(x)
			while i <= terminos:
				print "Terminos: "+ str(i) + "    cos("+str(x)+") = "+str(cos_aprox(x,i)) + "            ERP: "+ str(calcula_error(math.cos(x),cos_aprox(x,i)))
				i+=1

		# Salir del programa
		elif opcion == 6:
			print "Terminando normalmente."
			return

# especificamos que solo debe ejecutarse el main 
# y no todo el archivo como script

if __name__ == "__main__":
    main()