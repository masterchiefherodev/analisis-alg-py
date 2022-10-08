from random import sample
# Importamos un Método de la biblioteca random para generar listas aleatorias

lista = list(range(100))  # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample
# (8 elementos aleatorios de la lista base)
vectorbs = sample(lista, 8)
print("El vector a ordenar es:", vectorbs)


def particionado(lista: list):
    # Se toma como pivote el elemento 0
    pivote = lista[0]
    # Elementos < que
    izq = []
    # Elementos > que
    der = []
    for i in range(1, len(lista)):
        if(lista[i] < pivote):
            izq.append(lista[i])
        else:
            der.append(lista[i])
    # Se devuelven tres parametros
    # izq : Una lista con los elementos < pivote
    # El pivote
    # der: Una lista con los elementos > pivote
    return izq, pivote, der


def quicksort(lista: list):
    # Si la lista tiene un solo elemento o menos se ha lledo al caso base y se debe devolver la lista
    if(len(lista) < 2):
        return lista
    # De lo contrario se iguala los tres retornos de particionado a variables con el mismo nombre pues tendrán esta misma función
    izq, pivote, der = particionado(lista)
    # Se llaman de forma recursiva a quicsort hasta agotar los casos
    return quicksort(izq) + [pivote] + quicksort(der)


print("El vector ordenado es (quicksort): ", quicksort(vectorbs))
