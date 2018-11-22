#ShellSort
import random




def NewRandomArray(tam):

    array = []

    for x in range(0,51):

    	array.insert(x,random.randint(0,49))

    return array

def ShellSort(array):

    salto = int(len(array)/2)

    while salto > 0:

        i = salto
        if i  < len(array):

            for i in range(len(array)):

                j = i - salto

                while j >= 0:

                    k = j + salto

                    if array[j] <= array[k]:

                        j = -1

                    else:

                        auxi = array[j]

                        array[j] = array[k]
                        array[k] = auxi

                        j -= salto

            salto = int(salto/2)

    return array


array = NewRandomArray(10)

print()
print("Arreglo original ---> ",array)
print()

print()
print("Arreglo ordenado ---> ",ShellSort(array))
print()
