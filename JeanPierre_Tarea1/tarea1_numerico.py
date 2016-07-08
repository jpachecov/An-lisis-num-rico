
# Esta funcion calcula la varianza de una lista de numeros
def varianza(x):
	if (len(x) <= 1):
		return
	media = 0
	for y in x:
		media+=y
	media = (media+0.)/len(x)

	suma = 0
	for y in x:
		suma+=(y-media)**2
	suma = (suma+0.)/len(x)
	
	return suma

# Calcula la desviacion estandar usando la funcion anterior
def desviacion_estandar(x):
	if(len(x) <= 1) : 
		return
	return pow(varianza(x),1/2.)

# main() 
# loop principal
def main():

	salida = 1

	while(salida):
		print("Escribe una opción")
		print("1. Resolver problema de tarea.")
		print("2. Encontrar varianza y desviación estandar de un conjunto de puntos dado.")
		print("3. Salir")

		try:
			opcion = int(raw_input())			
		except ValueError:
			print "\n\nEsa opcion no es valida!"
			print "intenta de nuevo...\n\n"
			continue

		A = [5,2,6,3]

		# Mostramos la solucion al problema especifico
		if(opcion == 1):

			print "\n"
			print "Lista de cantidad de personas que conforman una familia:"
			print A
			print "varianza = ", varianza(A)
			print "desviacion estandar = ", desviacion_estandar(A), "\n"
		
		# Leemos lista y calculamos lo debido
		if(opcion == 2):
			
			bien = False
			while(not(bien)):
				print "\n"
				print "Escribe la lista de puntos y oprime enter, por ejemplo:"
				print "2 3 4 5.2 6 7.89 .9 .1 10 \n"
				
				lst = []
				try:
					lst = map(float, raw_input().split())
				except ValueError:
					print "\n\nEscribiste algo que no es un numero!"
					print "intenta de nuevo...\n"
					continue
				
				bien = True
				print "\n\n"
				print "lista ", lst
				print "varianza = ", varianza(lst)
				print "desviacion estandar =", desviacion_estandar(lst), "\n"
		
		# Terminamos la ejecución del bucle principal
		if(opcion == 3):
			salida = 0


# especificamos que solo debe ejecutarse el main 
# y no todo el archivo como script
if __name__ == "__main__":
    main()