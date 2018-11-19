
#Listas enlazadas
i = 0

class Nodo(object):

	def __init__(self,data):
		self.data = data
		self.next = None

	# def get_data(self):
	# 	return self.data
	
def push(q,i,p):
	
	if i < 5:
		if q.next != None:
			
			print("Ingresa el dato")
			data = input()
			p = Nodo(data)
			q.next = p
			q = p
			i += 1

			return q,p,i

		else:

			print("Ingresa el dato")
			data = input()	
			p = Nodo(data)
			q.next = p
			q = p
			i += 1

			return q,p,i

	else:
		print("Lista llena")

		return menu(r,q,i,p)

def peek_all(r,q,i):
	cont_local = 0
	q = r
	while cont_local < i+1:
		print(q.data)
		if q.next != None:
			
			q = q.next
		else:
			return 0

def peek_last(r,q,p):
	print(p.data)
	return 0

def peek_first(r,q):
	print(r.next.data)
	return 0

def peek_if(r,q,i):
	cont_local = 0
	q = r

	comp = input("Ingresa el dato a comprobar")
	while cont_local < i+1:

		if q.next != None:
			if comp == q.data:
				print("El dato esta en la lista")
				return 0
			else:
				print("-"*25)
				q = q.next
		else:

			return 0

# def pop(r,q,i,p):
# 	cont_local = 0
# 	q = r.next
# 	helpy_last = r
# 	helpy_front = q.next

# 	comp = input("Ingresa el dato a eliminar --->")
# 	while cont_local < i+1:

# 		if q.next != None:
# 			if comp == r.data:
# 				print("No se puede eliminar la Raiz")
# 				return 0

# 			else:
# 				if comp == q.data and comp != r.next.data:
# 					helpy_last.next = helpy_front
# 					q.next = None
# 					i -=1
# 					return i

# 				elif comp == r.next.data:
# 					r.next = helpy_front
# 					i -=1
# 					print("Dato eliminado")

# 					return i



# 				else:

# 					print("-"*25)
# 					helpy_last = helpy_last.next
# 					q = helpy_last.next
# 					helpy_front = q.next
# 		else:
# 			if q.next == None and comp == q.data:
# 				helpy_last.next = None
# 				q = r
# 				i -=1
# 				print("Dato eliminado")
# 				return i
# 			else:
# 				print("El dato no esta en la lista")
# 			return 0

#inicio

r = Nodo("Raiz")
q = r
p = r

def  menu(r,q,i,p):
	while True:

		print("1.-Agregar un dato")
		print("2.-Imprimir la lista")
		print("3.-Imprimir el ultimo dato agregado")
		print("4.-Imprimir el primer dato agregado")
		print("5.-Comprobar si hay un dato en la lista")
		#print("6.-Eliminar un dato")
		print("0.-Salir del programa")

		opcion = int(input())

		if opcion == 1:

			q,p,i = push(q,i,p)

		if opcion == 2:
			peek_all(r,q,i)


		if opcion == 3:
			peek_last(r,q,p)


		if opcion == 4:
			peek_first(r,q)


		if opcion == 5:
			peek_if(r,q,i)


		if opcion == 6:
			i = pop(r,q,i,p)



		if opcion == 0:

			print("Adios")
			return 0

menu(r,q,i,p)
