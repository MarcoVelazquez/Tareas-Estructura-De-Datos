#Colas dobles o Bicolas
#Push

cont = 0

def New_cola():
	Cola = [0,0,0,0,0,0,0,0,0,0]

	first_front = 10
	last_front = 10

	first_back = 0
	last_back = 0

	print(Cola)

	return Cola,first_front,last_front,first_back,last_back

def Push_front(Cola_,last_front, last_back,cont):
	if Cola_[last_front-1] == 0:
		if last_front == 0:
			#del(Cola_[last_front-1])
			print("-" * 25)
			print("Ingresa el numero")
			print("-" * 25)
			item = int(input())
			Cola_[last_front-1] = item
			last_front = 10
			print(Cola_)
			return Cola_,last_front,cont
		else:
			#del(Cola_[last_front-1])
			print("-" * 25)
			print("Ingresa el numero")
			print("-" * 25)
			item = int(input())
			Cola_[last_front-1] = item
			last_front -= 1
			print(Cola_)
			return Cola_,last_front,cont

	else:
		if cont == 10:
			print("Cola llena")
			cont = 0
			return Cola_,last_front,cont
		else:
			if last_front == 0:
				last_front = 10
				return Push_front(Cola_,last_front, last_back,cont)
			else:
				print("-")
				last_front -= 1
				cont += 1
				return Push_front(Cola_,last_front, last_back,cont)

def Push_last(Cola_,last_front,last_back,cont):
	
	if Cola_[last_back] == 0:
		if last_back == 9:
			print("-" * 25)
			print("Ingresa el numero")
			print("-" * 25)
			item = int(input())
			Cola_[last_back] = item
			last_back = 0
			print(Cola_)
			return Cola_,last_back,cont
		else:
			print("-" * 25)
			print("Ingresa el numero")
			print("-" * 25)
			item = int(input())
			Cola_[last_back] = item
			last_back +=1
			print(Cola_)
			return Cola_,last_back,cont

	else:
		if cont == 9:
			print("Cola llena")
			cont = 0
			return Cola_,last_back,cont
		else:
			if last_back == 9:
				last_back = 0
				return Push_last(Cola_,last_front, last_back,cont)
			else:
				print("-")
				last_back += 1
				cont += 1
				return Push_last(Cola_,last_front, last_back,cont)

# def Pop_front(Cola_,first_front,first_back,cont):
# 	if Cola_[first_front-1] == 0:
# 		if cont == 10:
# 			print("Cola vacia")
# 			cont = 0
# 			return Cola_,first_front,cont
# 		else:
# 			if first_front == 0:
# 				first_front = 10

# 				return Pop_front(Cola_,first_front,first_back,cont)
# 			else:
# 				first_front -= 1
# 				cont += 1
# 				return Pop_front(Cola_,first_front,first_back,cont)
# 	else:
# 		Cola_[first_front-1] = 0
# 		print(Cola_)
# 		cont = 0
# 		first_front = 10
# 		return Cola_,first_front,cont

# def Pop_last(Cola_,first_front,first_back,cont):
# 	if Cola_[first_back] == 0:
# 		if cont == 10:
# 			print("Cola vacia")
# 			cont = 0
# 			return Cola_,first_back,cont
# 		else:
# 			if first_back == 10:
# 				first_back = 0

# 				return Pop_last(Cola_,first_front,first_back,cont)
# 			else:
# 				first_back += 1
# 				cont += 1
# 				return Pop_last(Cola_,first_front,first_back,cont)
# 	else:
# 		print("Si entro")
# 		Cola_[first_back] = 0
# 		print(Cola_)
# 		cont = 0
# 		first_back = 0
# 		return Cola_,first_back,cont


def Menu(cont):
	while True:
		print("1.-Crear cola")
		print("2.-Anadir un numero al comienzo de la cola")
		print("3.-Anadir un numero al final de la cola")
		# print("4.-Eliminar un dato al comienzo de la cola")
		# print("5.-Eliminar un dato al final de la cola")
		print("0.-Salir")

		Opcion = int(input())

		if Opcion == 1:
			Cola_,first_front,last_front,first_back,last_back = New_cola()

		elif Opcion == 2:
			Cola_,last_front,cont= Push_front(Cola_,last_front,last_back,cont)

		elif Opcion == 3:
			Cola_,last_back,cont = Push_last(Cola_,last_front,last_back,cont)

		# elif Opcion == 4:

		# 	Cola_,first_front,cont = Pop_front(Cola_,first_front,first_back,cont)

		# elif Opcion == 5:

		# 	Cola_,first_back,cont = Pop_last(Cola_,first_front,first_back,cont)

		if Opcion == 0:
			return 0
	
Menu(cont)