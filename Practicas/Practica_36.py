import random

#Búsqueda secuencial

array = []

for i in range(0,50):

	array.insert(i,random.randint(0,50))



print()
print("Ingresa el número a buscar en el rango de 1 a 50 ---> ")
print()

num = int(input())


def Busqueda_secuencial(array,num):
	
	for i in range(len(array)):

		if num == array[i]:

			print()
			print("Número encontrado en la posición ",i)
			print()

			return 0

		
	print()
	print("El número no se ha encontrado")
	print()



print()
Busqueda_secuencial(array,num)
print()

print()
print("Arreglo completo: ")
print()
print(array)
print()

