def New_cola():
	Cola = [0,0,0,0,0]
	first = 5
	last = 5
	print(Cola)
	return Cola,first,last

def Push(Cola_,last,first):
	last -= 1
	if Cola_[last] == 0:
		

		if last == 4:
			del(Cola_[last])
			print("-" * 25)
			print("Ingresa el numero")
			print("-" * 25)
			item = int(input())
			Cola_.insert(last,item)

			#last -= 1

			print(Cola_)

			return Cola_,last
		
		elif last == 3:
			del(Cola_[last])
			
			print("-" * 25)
			print("Ingresa el numero")
			print("-" * 25)
			item = int(input())
			Cola_.insert(last,item)
			print(Cola_)
			#last -= 1

			return Cola_,last

		elif last == 2:
			del(Cola_[last])
			print("-" * 25)
			print("Ingresa el numero")
			print("-" * 25)
			item = int(input())
			Cola_.insert(last,item)
			print(Cola_)
			#last -= 1
			return Cola_,last

		elif last == 1:
			del(Cola_[last])
			print("-" * 25)
			print("Ingresa el numero")
			print("-" * 25)
			item = int(input())
			Cola_.insert(last,item)
			print(Cola_)
			#last -= 1

			return Cola_,last
					
		elif last == 0:
			del(Cola_[last])
			print("-" * 25)
			print("Ingresa el numero")
			print("-" * 25)
			item = int(input())
			Cola_.insert(last,item)
			print(Cola_)
			#last -= 1

			return Cola_,last
	else:
		if Cola_[last] == 0:
			if last == 4:
				del(Cola_[last])
				print("-" * 25)
				print("Ingresa el numero")
				print("-" * 25)
				item = int(input())
				Cola_.insert(last,item)

				#last -= 1

				print(Cola_)

				return Cola_,last
			
			elif last == 3:
				del(Cola_[last])
				
				print("-" * 25)
				print("Ingresa el numero")
				print("-" * 25)
				item = int(input())
				Cola_.insert(last,item)
				print(Cola_)
				#last -= 1

				return Cola_,last

			elif last == 2:
				del(Cola_[last])
				print("-" * 25)
				print("Ingresa el numero")
				print("-" * 25)
				item = int(input())
				Cola_.insert(last,item)
				print(Cola_)
				#last -= 1
				return Cola_,last

			elif last == 1:
				del(Cola_[last])
				print("-" * 25)
				print("Ingresa el numero")
				print("-" * 25)
				item = int(input())
				Cola_.insert(last,item)
				print(Cola_)
				#last -= 1

				return Cola_,last
						
			elif last == 0:
				del(Cola_[last])
				print("-" * 25)
				print("Ingresa el numero")
				print("-" * 25)
				item = int(input())
				Cola_.insert(last,item)
				print(Cola_)
				#last -= 1

				return Cola_,last

		else:
			last = 5
			print("Cola llena, ejecutar un push para continuar")


			
		

	return Cola_,last
	
def Pop(Cola_,first,last):
	first -= 1
	Cola_[first] = 0

	print("Dato fuera de la cola")

	print(Cola_)
	
	if first == -1:
		first = 5

		return Pop(Cola_,first,last)
	
	return Cola_,first,last

def Peek_all(Cola_):
 	print("Cola circular",Cola_)
 	return 0

def Peek_last(Cola_,last):
 	print("Ultimo dato:",Cola_[last])
 	return 0

def Peek_first(Cola_,first):
 	print("primer dato",Cola_[first])
 	return 0

def Peek_equal(Cola_):
	print("Introduce el dato a comparar")
	dato = int(input())
	for i in Cola_:

		if i == dato:
			print("Dato en la cola")

 	return 0

def Menu():
	while True:
		print("1.-Crear cola")
		print("2.-Anadir un numero a la cola")
		print("3.-Sacar un numero de la cola")
		print("4,-Imprimir la cola")
		print("5.-Imprimir el primer dato")
		print("6.-imprimir el ultimo dato")
		print("7.-Preguntar si exite un dato dentro de la cola")
		print("8.-Salir")

		Opcion = int(input())

		if Opcion == 1:
			Cola_,first,last = New_cola()

		if Opcion == 2:
			Cola_,last = Push(Cola_,last,first)

		if Opcion == 3:
			Cola_,first,last = Pop(Cola_,first,last)

		if Opcion == 4:
			Peek_all(Cola_)

		if Opcion == 5:
			Peek_first(Cola_,first)

		if Opcion == 6:
			Peek_last(Cola_,last)

		if Opcion == 7:
			Peek_equal(Cola_)

		if Opcion == 8:
			return 0
			





Menu()

