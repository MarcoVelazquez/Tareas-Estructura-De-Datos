import random

#Búsqueda binaria


#Función que genera un arreglo con números aleatorios
def NewRandomArray(tam):
	array = []

	for i in range(0,tam):

		array.insert(i,random.randint(0,tam))

	return array

#Función para ordenar arrays
def MergeSort(Array):

	len_Array = len(Array)

	#Primer división del array principal

	pibote = int(len(Array)/2)

	#Arreglo para la parte izquierda del arreglo

	left = []

	#Arreglos que dividen la parte izquierda ya dividida

	left_l = []

	left_r = []

	#Arreglo para la parte derecho del arreglo

	right = []

	#Arreglos que dividen la parte derecho ya dividida

	right_l = []

	right_r = []

	#Contador que guia el acceso al arregl original

	i = 0

	#Llenado del arreglo que representa a parte izquerda

	for j in range(pibote):


		left.insert(j,Array[i])

		del(Array[i])

		
	

	#Llenado del arreglo que representa a parte derecha

	for j in range(pibote):

		right.insert(j,Array[i])

		del(Array[i])

		


	#Separación de la parte izquierda del arreglo en otras dos partes pasando primero el llamado 'pibote', que nos servira para partir a la mitad esta parte del arreglo
	pibote = int(len(left)/2)
	i = 0

	#iteración donde se llena la división izquierda

	for x in range(pibote):

		left_l.insert(x,left[i])

		i += 1

	#iteración donde se llena la división derecha

	for x in range(pibote,len(left)):

		left_r.insert(x,left[i])

		i += 1

	#Separación de la parte izquierda del arreglo en otras dos partes pasando primero el llamado 'pibote', que nos servira para partir a la mitad esta parte del arreglo
	pibote = int(len(right)/2)
	i = 0

	#iteración donde se llena la división derecha, de la división ya realizada antes.

	for x in range(pibote):

		right_l.insert(x,right[i])

		i += 1

	#iteración donde se llena la división izquierda, de la división ya realizada antes.

	for x in range(pibote,len(right)):

		right_r.insert(x,right[i])

		i += 1




	#En esta iteración se acomoda la parte izquierda de la primera particion del lado izquierdo

	for i in range(0,len(left_l)-1):

		for j in range(0,len(left_l)-1-i):

			if left_l[j] > left_l[j+1]:

				left_l[j],left_l[j+1] = left_l[j+1],left_l[j]


	#En esta iteración se acomoda la parte derecha de la primera particion del lado izquierdo

	for i in range(0,len(left_r)-1):

		for j in range(0,len(left_r)-1-i):

			if left_r[j] > left_r[j+1]:

				left_r[j],left_r[j+1] = left_r[j+1],left_r[j]

	#En esta iteración se acomoda la parte izquierda de la primera particion del lado derecho

	for i in range(0,len(right_l)-1):

		for j in range(0,len(right_l)-1-i):

			if right_l[j] > right_l[j+1]:

				right_l[j],right_l[j+1] = right_l[j+1],right_l[j]

	#En esta iteración se acomoda la parte derecha de la primera particion del lado derecho			

	for i in range(0,len(right_r)-1):

		for j in range(0,len(right_r)-1-i):

			if right_r[j] > right_r[j+1]:

				right_r[j],right_r[j+1] = right_r[j+1],right_r[j]



	#indices que serán utilizados en la siguiente iteración

	l = 0
	r = 0

	#En este ciclo se van a comparar las dos mitades del lado izquierdo, y serán acomodadas en orden en el arreglo que representa la mitad izquierda del arreglo original

	#El ciclo se realiza con el rango(tamaño) del arreglo que representa la parte izquierda del arreglo original
	for i in range(len(left)):


		#En esta condición se pregunta si el rango de las dos mitades a comparar es mayor a 0, para poder comparar los datos en ellos, si no lo es, pasara al 'else', donde introducira los datos sobrante(que tambien serán os mayores), en el arreglo donde los estamos acomodando
		if len(left_l) > 0 and len(left_r) > 0:

			#Aqui se comparan los datos en el indice actual de ambos arreglos, si se cumple la condición de que el dato de 'l' sea menor que el de 'r', el dato que de 'l' pasara al arreglo en donde estamos acomodando los datos 
			if left_l[l] < left_r[r]:

				#Se introduce el dato de 'l' al arreglo en donde se están acomodando los datos.
				left[i] = left_l[l]

				#El dato que introducimos al nuevo arreglo es eliminado de su arreglo original
				del(left_l[l])
					
			#Si no se cumple la condción anterior, se pasara a esta parte, y en vez de pasar el dato de 'l', al nuevo arreglo, hará las operaciones con el dato en el arreglo 'r'
			else:

				

				left[i] = left_r[r]

				del(left_r[r])

				
		#Una vez que el tamanño de alguno de los arreglos llegue a 0, se pasara a esta parte
		else:

			#Se pregunta si el tamaño del arreglo 'l' es igual a 0, si lo es, se entra a esta parte, y se mueve el dato de 'r' a el arreglo donde se estén acomodando los datos, y se elimina de su arreglo original
			if len(left_l) == 0:

				left[i] = left_r[r]

				del(left_r[r])

			#Si el tamaño de 'l' no es igual a 0, preguntará si el tamaño de 'r' si lo es, y si es correcto, se realizan las mismas acciones que se hicieron dentro de la condición anterior, pero utilizan 'l'
			elif len(left_r) == 0:

				left[i] = left_l[l]

				del(left_l[l])


	#En este ciclo se van a comparar las dos mitades del lado derecho, y serán acomodadas en orden en el arreglo que representa la mitad derecha del arreglo original

	#Se hace lo mismo que en el ciclo anterior, con la diferencia que aquí se realizaran los operaciones con la mitad derecha del arreglo original

	for i in range(len(right)):


		
		if len(right_l) > 0 and len(right_r) > 0:

			
			if right_l[l] < right_r[r]:

				right[i] = right_l[l]

				del(right_l[l])
					

			else:

				

				right[i] = right_r[r]

				del(right_r[r])

				
		else:

			if len(right_l) == 0:

				right[i] = right_r[r]

				del(right_r[r])


			elif len(right_r) == 0:

				right[i] = right_l[l]

				del(right_l[l])



	#Ordenación final

	for i in range(len_Array):


		
		if len(left) > 0 and len(right) > 0:

			
			if left[l] < right[r]:


				Array.insert(i,left[l])
				#Array[i] = left[l]

				del(left[l])
					

			else:

				
				Array.insert(i,right[r])
				#Array[i] = right[r]

				del(right[r])

				
		else:

			if len(left) == 0:

				Array.insert(i,right[r])
				#Array[i] = right[r]

				del(right[r])


			elif len(right) == 0:

				Array.insert(i,left[l])
				#Array[i] = left[l]

				del(left[l])

	



				
	# print(left," ",right)
	# print()
	# print()


	return Array

#Función que encontrara el dato a buscar
def Busqueda_binaria(array,num):

	pibote = int(len(array)/2)

	if pibote == 0:

		print()
		print("El número no se ha encontrado")
		print()

		return 0

	if num == array[pibote]:

		print()
		print("El número está")
		print()

		return 0

	elif num < array[pibote]:

		short_array = []

		for i in range(0,pibote):

			short_array.insert(i,array[i]) 

		array = short_array

		return Busqueda_binaria(array,num)
		

	elif num > array[pibote]:

		short_array = []

		for i in range(pibote,len(array)):

			short_array.insert(i,array[i]) 

		array = short_array

		return Busqueda_binaria(array,num)

def Menu():

	while  True:
		
		print()
		print("			<<<Búsqueda binaria>>>")
		print()
		print()
		print("			       <<Menu>>")
		print()

		print()
		print("		1.-Buscar un número en un array aleatorio")
		print()
		print("		0.-Salir")

		select = int(input())

		if select == 1:

			array = NewRandomArray(50)

			array = MergeSort(array)

			print()
			print("		Ingresa el número a buscar")
			print()

			num = int(input())

			# print()
			# print("Arreglo aleatorio")
			# print(array)
			# print()

			Busqueda_binaria(array,num)

			

		if select == 0:

			return False

Menu()