item = 0
i = 0
def New_Cola():
	Cola = [0,0,0,0,0]
	i = 4
	
	return Cola,i

def Pop(Cola_,i):
	Cola_[4] = Cola_[3]
	Cola_[3] = Cola_[2]
	Cola_[2] = Cola_[1]
	Cola_[1] = Cola_[0]
	Cola_[0] = 0
	i += 1
	print("-" * 25)
	print(Cola_)
	print("-" * 25)

	return Cola_, i

def Push(Cola_,item,i):
	if i == 4:
		print("-" * 25)
		print("Ingresa el numero")
		print("-" * 25)
		item = int(input())
		Cola_[i] = item
		i -= 1
		
		
	elif i == 3:
		print("-" * 25)
		print("Ingresa el numero")
		print("-" * 25)
		item = int(input())
		Cola_[i] = item
		i -= 1
		

	elif i == 2:
		print("-" * 25)
		print("Ingresa el numero")
		print("-" * 25)
		item = int(input())
		Cola_[i] = item
		i -= 1
		
	elif i == 1:
		print("-" * 25)
		print("Ingresa el numero")
		print("-" * 25)
		item = int(input())
		Cola_[i] = item
		i -= 1
		
	elif i == 0:
		print("-" * 25)
		print("Ingresa el numero")
		print("-" * 25)
		item = int(input())
		Cola_[i] = item
		i -= 1
		

		

	return Cola_,i,item

def Menu(item,i):
	while True:
		print("1.-Crear cola")
		print("2.-Anadir un numero a la cola")
		print("3.-Sacar un numero de la cola")
		print("4.-Imprimir cola")
		print("5.-Comprobar si un dato esta en la cola")
		print("6.-Mostrar el ultimo dato ingresado en la cola")
		print("7.-Mostrar el proximo dato a salir")
		print("8.-Salir")

		Opcion = int(input())

		if Opcion == 1:
			Cola_,i = New_Cola()
			print("-" * 25)
			print("<<Cola creada>>")
			print(Cola_)
			print("-" * 25)
		elif Opcion == 2:
			if i == 4:
				Cola_,i,item = Push(Cola_,item,i)
				print("-" * 25)
				print(Cola_)
				print("-" * 25)
			elif i == 3:
				Cola_,i,item = Push(Cola_,item,i)
				print("-" * 25)
				print(Cola_)
				print("-" * 25)
			elif i == 2:
				Cola_,i,item = Push(Cola_,item,i)
				print("-" * 25)
				print(Cola_)
				print("-" * 25)
			elif i == 1:
				Cola_,i,item = Push(Cola_,item,i)
				print("-" * 25)
				print(Cola_)
				print("-" * 25)
			elif i == 0:
				Cola_,i,item = Push(Cola_,item,i)
				print("-" * 25)
				print(Cola_)
				print("-" * 25)
			else:
				print("-" * 25)
				print("Cola llena")
				print("-" * 25)
				
		elif Opcion == 3:
			Cola_,i = Pop(Cola_,i)
			if i > 4:
				print("-" * 25)
				print("VACIA")
				print("-" * 25)
			
		elif Opcion == 4:
			Peek(Cola_,item,i)
		
		elif Opcion == 5:
			print("-" * 25)
			print("ingresa el dato comprobar")
			print("-" * 25)
			dato = int(input()) 
			
			Peek_if(Cola_,dato)

		elif Opcion == 6:
			print("-" * 25)
			print("El ultimo dato ingresado fue:")
			Peek_first(Cola_)
			print("-" * 25)

		elif Opcion == 7:
			print("-" * 25)
			print("El proximo dato a salir es:")
			Peek_last(Cola_)
			print("-" * 25)


		elif Opcion == 8:
			return 0	

def Peek(Cola_,item,i):
	print("-" * 25)
	print(Cola_)
	print("-" * 25)
	return 0

def Peek_last(Cola_):
	
	print(Cola_[4])
	
	return 0

def Peek_first(Cola_):
	
	print(Cola_[0])
	
	return 0

def Peek_if(Cola_,dato):
	 for j in Cola_:
	 		if j == dato:
	 			print("-" * 25)
	 			print("<<El dato esta en la cola>>")
	 			print("-" * 25)
	 			return j
	 		else:
	 			print("-" * 25)
	 			print("El dato no esta en la cola")
	 			print("-" * 25)
	 			return 0
	 		

Menu(item,i)



	
