#Examen unidad 3
#Ejercicio para llevar

#listas doblemente enlazadas

class Nodo(object):

	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None


#inicio

#Raiz izquierda
front = Nodo("Front") 


#Punteros de la raiz izquierda
front_pointer = front
front_helper = front

#Raiz derecha
back = Nodo("Back")	 

#Punteros de la raiz derecha
back_pointer = back
back_helper = back

#Enlaces iniciales
front.right = back
front_pointer.right = back
front_helper.right = back

back.left = front
back_pointer.left = front
back_helper.left = front

#METODOS

#Metodo 'push' del lado izquierdo
def push_front(front,front_pointer,front_helper,back_pointer,back_helper,item):
	#print("-"*30)
	#print("Ingresa el dato a agregar a la lista")
	# print()
	# item = input()
	# print("-"*30)

	front_pointer = Nodo(item)
	front_helper.right = front_pointer
	front_pointer.left = front_helper
	front_helper = front_pointer
	front_helper.right = back_helper
	back_helper.left = front_helper


	return front_pointer,front_helper

#Metodo 'push' del lado derecho
def push_back(front,front_pointer,front_helper,back_pointer,back_helper):
	print("-"*30)
	print("Ingresa el dato a agregar a la lista")
	print()
	item = input()
	print("-"*30)

	back_pointer = Nodo(item)
	back_helper.left = back_pointer
	back_pointer.right = back_helper
	back_helper = back_pointer
	back_helper.left = front_helper
	front_helper.right = back_helper


	return back_pointer,back_helper

#Lectura desde el lado derecho
def peek_all_back(back_helper):
	back_helper = back
	while Nodo:
		if back_helper.left != None:
				print(back_helper.data)
				back_helper = back_helper.left
		else:
			print(back_helper.data)
			return 0

#Lectura desde el lado izquierdo
def peek_all_front(front_helper):
	front_helper = front
	while Nodo:
		if front_helper.right != None:
				print(front_helper.data)
				front_helper = front_helper.right
		else:
			print(front_helper.data)
			return 0

#Metodo que comprueba si hay un dato en la lista
def peek_if(front_helper,comp):
	
	front_helper = front
	while Nodo:
		if front_helper.right != None:
				if comp == front_helper.data:
					print("El dato", comp, " esta en la lista")
					return 0
				else:
					front_helper = front_helper.right
		else:
			print("El dato", comp, " no esta en la lista")
			return 0

def pop(front_helper,front,comp):
	
	front_helper = front.right
	front_helper_back = front
	front_helper_front = front_helper.right


	while Nodo:
		if front_helper.right != None:
				if comp == "Front" or comp == "Back":
					print("   No se pueden eliminar las raices")
				else:
					if comp == front_helper.data and comp != front.right.data:
						front_helper_back.rigth = front_helper_front
						front_helper_front.left = front_helper_front
						front_helper.right = None
						front_helper.left = None
						print("El dato", comp, " ha sido eliminado")
						
						return 0

					elif comp == front.right.data:

						front.right = front_helper_front
						front_helper_front.left = front
						print("El dato", comp, " ha sido eliminado")

						return 0



					
					else:
						
						front_helper_back = front_helper_back.right
						front_helper = front_helper_back.right
						front_helper_front = front_helper_front.right
		else:
			print("El dato", comp, " no esta en la lista")
			return 0




def menu(front_pointer,front_helper,front,back):
	while True:
		

		print()
		print("---Selecciona una opcion---")
		print()

		print("1.-Instruccion No.1: Introducir a la lista los datos del 1 al 9")
		print("2.-Instruccion No.2: Leer la lista de izquierda a derecha")
		print("3.-Instruccion No.3: Leer la lista de derecha a izquierda")
		print("4.-Instruccion No.4: Insertar 10,11 y 13")
		print("5.-Instruccion No.5: Eliminar 8 y 1")
		print("6.-Instruccion No.6: Leer raiz")
		print("7.-Instruccion No.7: Leer final de la lista del lado derecho e izquierdo")
		print("8.-Instruccion No.8: Buscar 0,7,8 y 1")
		print()
		print("0.-Salir del programa")

		print()

		opcion = int(input("--->>>   "))

		if opcion == 1:

			
			front_pointer,front_helper = push_front(front,front_pointer,front_helper,back_pointer,back_helper,1)
			front_pointer,front_helper = push_front(front,front_pointer,front_helper,back_pointer,back_helper,2)
			front_pointer,front_helper = push_front(front,front_pointer,front_helper,back_pointer,back_helper,3)
			front_pointer,front_helper = push_front(front,front_pointer,front_helper,back_pointer,back_helper,4)
			front_pointer,front_helper = push_front(front,front_pointer,front_helper,back_pointer,back_helper,5)
			front_pointer,front_helper = push_front(front,front_pointer,front_helper,back_pointer,back_helper,6)
			front_pointer,front_helper = push_front(front,front_pointer,front_helper,back_pointer,back_helper,7)
			front_pointer,front_helper = push_front(front,front_pointer,front_helper,back_pointer,back_helper,8)
			front_pointer,front_helper = push_front(front,front_pointer,front_helper,back_pointer,back_helper,9)

			print()
			peek_all_front(front_helper)
			print()
			print("   *Instruccion completa*")
			print()

		if opcion == 2:
			print()
			peek_all_front(front_helper)
			print()
			print("   *Instruccion completa*")

		if opcion == 3:
			print()
			peek_all_back(back_helper)
			print()
			print("   *Instruccion completa*")

		if opcion == 4:

			front_pointer,front_helper = push_front(front,front_pointer,front_helper,back_pointer,back_helper,10)
			front_pointer,front_helper = push_front(front,front_pointer,front_helper,back_pointer,back_helper,11)
			front_pointer,front_helper = push_front(front,front_pointer,front_helper,back_pointer,back_helper,13)

			print()
			peek_all_front(front_helper)
			print()
			print("   *Instruccion completa*")
			print()

		if opcion == 5:
			print()
			pop(front_helper,front,8)
			print()
			pop(front_helper,front,1)
			print()
			peek_all_front(front_helper)
			print()
			print("   *Instruccion completa*")
			print()

		if opcion == 6:
			print()
			print("   Raiz izquierda:  ", front.data)
			print("   Raiz derecha:  ", back.data)
			print()
			print("   *Instruccion completa*")
			print()

		if opcion == 7:
			print()
			print("   Final izquierdo:   ", front.right.data)
			print("   Final derecho:   ", back.left.data)
			print()
			print("   *Instruccion completa*")
			print()

		if opcion == 8:
			print()
			peek_if(front_helper,0)
			print()
			peek_if(front_helper,7)
			print()
			peek_if(front_helper,8)
			print()
			peek_if(front_helper,1)
			print()
			print("   *Instruccion completa*")
			print()


		if opcion == 0:
			print()
			print("   <<<Ciao>>>")
			print()
			return 0
		
			
print()
print("   <<<Examen unidad 3>>>")
print()
print("Marco Antonio Velazquez Figueroa   17212193")
print()
print("   <<<Ejercicio para llevar>>>")
print()
				

menu(front_pointer,front_helper,front,back)
