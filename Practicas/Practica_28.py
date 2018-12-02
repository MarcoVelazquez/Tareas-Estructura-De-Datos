cont_nodes = 1
cont_local = 0

print()
print("   <<<Arbol binario>>>")
print()

print()
print("   <<<Marco Antonio Velzquez Figueroa>>>")
print()

class Nodo(object):

	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None


#Inicio

#Se crea el nodo 'raiz'
r = Nodo("A")
#Los punteros se inician en la raiz para poder moverlos
p = r
q = r
olrhain = r


#Funcion que va a agregar los nodos y creara los enlaces
def push(p,q,olrhain,cont_nodes):

	print()
	print("Selecciona una opcion")
	print()

	#Aqui se le da a legir a usuario donde quiere agregar su nodo, si al lado derecho, o al lado izquierdo

	print()
	print("1.-Añadir dato del lado derecho")
	print("2.-Añadir dato del lado izquierdo")
	print("3.-Regresar al menu")
	print()

	print()
	opcion = int(input("---> "))
	print()

	if opcion == 1:
		if q.right == None:

			print()
			print("Ingresa el dato a agregar")
			print()

			print()
			data = input("---> ")
			print()

			p = Nodo(data)
			olrhain = q
			q.right = p

			cont_nodes += 1

			print()
			print("   Dato agregado exitosamente")
			print()

			return cont_nodes
		else:
			olrhain = q
			q = olrhain.right

			return push(p,q,olrhain,cont_nodes)

	elif opcion == 2:
		if q.left == None:

			print()
			print("Ingresa el dato a agregar")
			print()

			print()
			data = input("---> ")
			print()

			p = Nodo(data)
			olrhain = q
			q.left = p

			cont_nodes += 1

			print()
			print("   Dato agregado exitosamente")
			print()

			return cont_nodes
		else:
			olrhain = q
			q = olrhain.left

			return push(p,q,olrhain,cont_nodes)

	elif opcion == 3:
		return p,q,olrhain


def GoLeft(nodo):
    if(nodo.left!=None):
        nodo=nodo.left
        Ino(nodo)

#Metodo para recorrer el nodo a su .right, siempre y cuando este no sea None
def GoRight(nodo):
    if(nodo.right!=None):
        nodo=nodo.right
        Ino(nodo)

#Metodo para recorrer todo el arbol en InOrden
#Primero recorrera el subarbol izquierdo
#Despues imprimir la raiz
#Y al final recorrera el subarbol derecho
def Ino(nodo):
    if nodo == None:
        return
    else:
        Ino(nodo.left)
        print(nodo.data)
        Ino(nodo.right)

def GoLeft(nodo):
    if nodo == None:
        return
    else:
        GoLeft(nodo.left)
        print(nodo.data)
        GoLeft(nodo.right)

#Metodo para recorrer el nodo a su .right, siempre y cuando este no sea None
def GoRight(nodo):
    if(nodo.right!=None):
        nodo=nodo.right
        Pos(nodo)

#Metodo para recorrer todo el arbol en PostOrden
#Primero recorrera el subarbol izquierdo
#Despues recorrera el subarbol derecho
#Al final imprimira la raiz
def Pos(nodo):
    if nodo == None:
        return
    else:
        Pos(nodo.left)
        Pos(nodo.right)
        print(nodo.data)

#Metodo para recorrer el nodo a su .left, siempre y cuando este no sea None
def GoLeft(nodo):
    if(nodo.left!=None):
        nodo=nodo.left
        Pre(nodo)

#Metodo para recorrer el nodo a su .right, siempre y cuando este no sea None
def GoRight(nodo):
    if(nodo.right!=None):
        nodo=nodo.right
        Pre(nodo)

#Metodo para recorrer todo el arbol en PreOrden
#Primero imprimira la raiz
#Despues recorrera el subarbol izquierdo
#Y al final recorrera el subarbol derecho
def Pre(nodo):
    if nodo == None:
        return
    else:
        print(nodo.data)
        Pre(nodo.left)
        Pre(nodo.right)



def menu(p,q,olrhain,cont_nodes):

	while True:

		print()
		print("   Selecciona una opcion")
		print()

		print("1.-Añadir un dato")
		#print("2.-Eliminar un dato")
		print("3.-Lectura 'infijo'")
		#print("4.-Lectura 'PostOrden'")
		print("5.-Lectura 'PreOrden'")
		print()
		print("0.-Salir")
		print()

		print()
		opcion = int(input("---> "))
		print()

		if opcion == 1:

			cont_nodes = push(p,q,olrhain,cont_nodes)

		elif opcion == 2:

			print()
			print("   Funcion en proceso")
			print()

		elif opcion == 3:

			print()
			print("   -Lectura 'infijo'-")
			print()

			#peek_infijo(p,q,olrhain,cont_nodes,cont_local)
			Ino(r)

		elif opcion == 4:

			print()
			print("		-Lectura 'PostOrden'")
			print()

			Pos(r)

		elif opcion == 5:

			print()
			print("		-Lectura 'PreOrden'")
			print()

			Pre(r)

		elif opcion == 0:

			print()
			print("   <<<Ciao>>>")
			print()

			return 0


menu(p,q,olrhain,cont_nodes)
