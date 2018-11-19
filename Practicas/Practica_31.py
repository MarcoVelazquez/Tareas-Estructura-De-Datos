import random

Array = []
datos_in = 0

for x in range(0,50):

	datos_in += 1

	Array.insert(x,random.randint(0,49))

def bubblesort(Array):

	comparaciones = 0
	intercambios = 0

	for i in range(0,len(Array)-1):

		for j in range(0,len(Array)-1-i):

			comparaciones += 1

			if Array[j] > Array[j+1]:

				Array[j],Array[j+1] = Array[j+1],Array[j]

				intercambios += 1

	# print()
		#print(Array)
	# print()

	print()
	print("Arreglo de ",datos_in," datos")
	print()
	print("comparaciones: ", comparaciones)
	print("intercambios: ", intercambios)
	print()

	return Array

print()
print("Arreglo aleatorio original --->  ",Array)
print()

print()
print("Arreglo aleatorio acomododado ---> ",bubblesort(Array))
print()






