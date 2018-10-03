pila = []
item = 0
i = 0
limite = 5

def Push(i,item,limite):
	if i < limite:
		print("-" * 25)
		print("Ingresa tu numero")
		item = int(input())
		print("-" * 25)
		pila.append(item) 
    	i=i+1 
    	print(pila)
    	print("-" * 25)

    	return i 



def Peek():
	print("-" * 25)
	print(pila)
	print("-" * 25)
	return 0

def Pop(i):
	if i >= 0:
		del(pila[i])
		print("-" * 25)
		print(pila)
		print("-" * 25)
		i -= 1
		return i

def Menu(i):
	while True:
		print("1.-Ingresar un dato a la pila")
		print("2.-Sacar un dato de la pila")
		print("3.-Mostrar la pila")
		print("4.-Salir")

		Opcion = int(input())

		if Opcion == 1:
			i = Push(i,item,limite)

		elif Opcion == 2:
			i = Pop(i)

		elif Opcion == 3:
			Peek(i) 

		else:
			return 0


Menu(i)