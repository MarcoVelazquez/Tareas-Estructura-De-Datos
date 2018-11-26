#Quicksort

import random

def NewRandomArray(tam):
	#array = [17,41,5,22,54,6,29,3,13]
	
	array = []

	for i in range(0,tam):
	
	 	array.insert(i,random.randint(0,tam))

	return array

def QuickSort(a,iz,de):

    i = iz
    j = de

    pivote = a[int((iz+de)/2)]

    while i <= j:

        while a[i] < pivote:

            i += 1

        while a[j] > pivote:

            j -= 1

        if i <= j:

            auxi = a[i]

            a[i] = a[j]
            a[j] = auxi

            i += 1
            j -= 1

    if j > iz:

        QuickSort(a,iz,j)

    if i < de:

        QuickSort(a,i,de)

    return a






def Menu():

	while True:

		print()
		print("			<<<QuickSort>>>")
		print()
		print()
		print("			   <<Menu>>")
		print()

		print()
		print("		1.-Ordenar un array aleatorio")
		print()
		print("		0.-Salir")
		print()

		print()
		select = int(input("Ingresa tu elección ---> "))
		print()

		if select == 1:

			array = NewRandomArray(100)

			print()
			print("Array original ---> ",array)
			print()

			print()
			print("Array ordenado ---> ",QuickSort(array,0,len(array)-1))
			print()

		elif select == 0:

			print()
			print("		   <<Chiao>>")
			print()

			return False


Menu()
