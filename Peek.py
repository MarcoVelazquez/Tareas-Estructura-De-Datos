pila = []
item = 0
i = 0

    
def push(item):
    pila.append(item)
    return 0

if i<=5:
	print("Introduce tu numero")
	item = int(input())
	push(item)
	i = i+1

	print("Introduce tu numero")
	item = int(input())
	push(item)
	i = i+1

	print("Introduce tu numero")
	item = int(input())
	push(item)
	i = i+1

	print("Introduce tu numero")
	item = int(input())
	push(item)
	i = i+1

	print("Introduce tu numero")
	item = int(input())
	push(item)
	i = i+1
	print("Pila llena")

def Peek(i):
	i -= 1
	print(pila[i])
	return i

print("El dato en el tope de la pila es:")
i = Peek(i)

print(i)





