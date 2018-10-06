#Ejercicio No.4

print("Tienda abierta, abrir fila, porfavor")

item = 0
i = 0
Cont_ = 1
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

def Push(Cola_,Cont_,i):
	if i == 4:
		print("-" * 25)
		print("Cliente en la fila")
		print("-" * 25)
		Cola_[i] = Cont_
		i -= 1
		Cont_ += 1
		
	elif i == 3:
		print("-" * 25)
		print("Cliente en la fila")
		print("-" * 25)
		Cola_[i] = Cont_
		i -= 1
		Cont_ += 1

	elif i == 2:
		print("-" * 25)
		print("Cliente en la fila")
		print("-" * 25)
		Cola_[i] = Cont_
		i -= 1
		Cont_ += 1
	elif i == 1:
		print("-" * 25)
		print("Cliente en la fila")
		print("-" * 25)
		Cola_[i] = Cont_
		i -= 1
		Cont_ += 1
	elif i == 0:
		print("-" * 25)
		print("Cliente en la fila")
		print("-" * 25)
		Cola_[i] = Cont_
		i -= 1
		Cont_ += 1
		

		

	return Cola_,i,Cont_

def Menu(item,i,Cont_):
	while True:
		print("1.-Abrir fila de clientes")
		print("2.-Un cliente entra")
		print("3.-Atender al siguiente cliente")
		print("4.-Estado de la fila")
		print("5.-Consultar el numero de clientes que se han formado en la fila")
		print("6.-Cerra fila, y cerrar tienda")

		Opcion = int(input())

		if Opcion == 1:
			Cola_,i = New_Cola()
			print("-" * 25)
			print("<<Fila abierta>>")
			print(Cola_)
			print("-" * 25)
		elif Opcion == 2:
			if i == 4:
				Cola_,i,Cont_ = Push(Cola_,Cont_,i)
				print("-" * 25)
				print(Cola_)
				print("-" * 25)
				
			elif i == 3:
				Cola_,i,Cont_ = Push(Cola_,Cont_,i)
				print("-" * 25)
				print(Cola_)
				print("-" * 25)
				
			elif i == 2:
				Cola_,i,Cont_ = Push(Cola_,Cont_,i)
				print("-" * 25)
				print(Cola_)
				print("-" * 25)
				
			elif i == 1:
				Cola_,i,Cont_ = Push(Cola_,Cont_,i)
				print("-" * 25)
				print(Cola_)
				print("-" * 25)
				
			elif i == 0:
				Cola_,i,Cont_ = Push(Cola_,Cont_,i)
				print("-" * 25)
				print(Cola_)
				print("-" * 25)
				
			elif i == -1:
				print("-" * 25)
				print("Fila llena")
				print("-" * 25)
				
		elif Opcion == 3:
			Cola_,i = Pop(Cola_,i)
			if i > 4:
				print("-" * 25)
				print("Fila vacia")
				print("-" * 25)
				i -= 1
			
		elif Opcion == 4:
			Peek(Cola_,i)


		elif Opcion == 5:
			print("Numero de clientes formados", Cont_ - 1)
		
		
		elif Opcion == 6:
			return False	

def Peek(Cola_,i):
	print("-" * 25)
	print(Cola_)
	print("-" * 25)
	return 0
	 		

Menu(item,i,Cont_)



	



