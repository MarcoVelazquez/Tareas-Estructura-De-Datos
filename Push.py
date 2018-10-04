item = 0
i = 0
def New_Cola():
	Cola = [0,0,0,0,0]
	i = 4
	
	return Cola,i

def Push(Cola_,item,i):
	if i == 4:
		print("-" * 25)
		print("Ingresa el numero")
		print("-" * 25)
		item = int(input())
		Cola_[i] = item
		i -= 1

		return Cola_,i,item
		
		
	elif i == 3:
		print("-" * 25)
		print("Ingresa el numero")
		print("-" * 25)
		item = int(input())
		Cola_[i] = item
		i -= 1

		return Cola_,i,item
		

	elif i == 2:
		print("-" * 25)
		print("Ingresa el numero")
		print("-" * 25)
		item = int(input())
		Cola_[i] = item
		i -= 1

		return Cola_,i,item
		
	elif i == 1:
		print("-" * 25)
		print("Ingresa el numero")
		print("-" * 25)
		item = int(input())
		Cola_[i] = item
		i -= 1

		return Cola_,i,item
		
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
		print("3.-Salir")

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
			return 0

Menu(item,i)



