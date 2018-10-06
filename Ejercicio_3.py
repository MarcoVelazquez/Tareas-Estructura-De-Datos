#Ejercicio No.3

cont_ = 0

def New_pila():
	pila = []
	i = 0
	return pila,i

def Push(pila,i,cont):
	pila.append(cont)
	print("Registro hecho")
	i += 1
	cont += 1
	return pila,i,cont

def Pop(pila,i):
	if i > 0:
		del(pila[i-1])
		i -= 1
		return pila,i
	else:
		print("No hay registros")
		return pila,i

def Menu(cont_):

	pila_,i = New_pila()

	while  True:
		print("1.-Registrar una migracion")
		print("2.-Obtener el registro de la migracion mas actual")
		print("3.-Salir")

		Opcion = int(input())

		if Opcion == 1:
			pila_,i,cont_ = Push(pila_,i,cont_)
			print(pila_)
		elif Opcion == 2:
			pila_,i = Pop(pila_,i)
			print(pila_)
			print("Ultimo registro obtenido")



		elif Opcion == 3:
			return False

Menu(cont_)