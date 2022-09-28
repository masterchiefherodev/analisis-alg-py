from random import sample
# Importamos un Método de la biblioteca random para generar listas aleatorias

lista = list(range(100))  # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample
# (8 elementos aleatorios de la lista base)
vectorbs = sample(lista, 8)
print("El vector a ordenar es:", vectorbs)


def bubblesort(lista: list):
    """Esta función ordenara el vector que le pases como argumento con el Método de Bubble Sort"""

  # Recorremos la lista para comparar los elementos
    for i in range(len(lista)):
        # Recorremos la lista para comparar los elementos uno a uno
        for j in range(0, len(lista)-i-1):
            # Revisa la matriz de 0 hasta n-i-1
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
            # Se intercambian si el elemento encontrado es mayor
    print("El vector ordenado es (bubblesort): ", lista)


def selectionsort(lista: list):
    """Esta función ordenara el vector que le pases como argumento con el Método Selection Sort"""

    for i in range(len(lista)):
        # Encontrar el minimo elemento de los restantes sin ordenar
        minimo = i
        for j in range(i+1, len(lista)):
            if lista[minimo] > lista[j]:
                minimo = j
        # Cambiamos el elemento minimo encontrado con el primer elemento de la matriz
        lista[i], lista[minimo] = lista[minimo], lista[i]
        # Repetimos el proceso hasta terminar
    print("El vector ordenado es (selección): ", lista)


def insertionsort(lista: list):
    """Esta función ordenara el vector que le pases como argumento con
    el Método Insertion Sort"""

    # Recorremos la lista de 1 hasta el largo total
    for i in range(1, len(lista)):

        elemento = lista[i]

        # Movemos los elementos de lista[0...i-1], que son mayores que el elemento
        # a una posición adelante de su posición actual
        j = i-1
        while j >= 0 and elemento < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = elemento
    print("El vector ordenado es (insersión): ", lista)


def quicksort(vectorbs, start=0, end=len(vectorbs) - 1):
    """Esta función ordenara el vector que le pases como argumento 
    con el Método Quick Sort"""

    def quick(vectorbs, start=0, end=len(vectorbs) - 1):

        if start >= end:
            return

        def particion(vectorbs, start=0, end=len(vectorbs) - 1):
            pivot = vectorbs[start]
            menor = start + 1
            mayor = end

            while True:
                # Si el valor actual es mayor que el pivot
                # está en el lugar correcto (lado derecho del pivot) y podemos
                # movernos hacia la izquierda, al siguiente elemento.
                # También debemos asegurarnos de no haber superado el puntero bajo, ya que indica
                # que ya hemos movido todos los elementos a su lado correcto del pivot
                while menor <= mayor and vectorbs[mayor] >= pivot:
                    mayor = mayor - 1

                # Proceso opuesto al anterior
                while menor <= mayor and vectorbs[menor] <= pivot:
                    menor = menor + 1

                # Encontramos un valor sea mayor o menor y que este fuera del arreglo
                # ó menor es más grande que mayor, en cuyo caso salimos del ciclo
                if menor <= mayor:
                    vectorbs[menor], vectorbs[mayor] = vectorbs[mayor], vectorbs[menor]
                    # Continua el bucle
                else:
                    # Salimos del bucle
                    break

            vectorbs[start], vectorbs[mayor] = vectorbs[mayor], vectorbs[start]

            return mayor

        p = particion(vectorbs, start, end)
        quick(vectorbs, start, p-1)
        quick(vectorbs, p+1, end)

    quick(vectorbs)
    print("El vector ordenado es (quicksort):", vectorbs)


# Test
selectionsort(vectorbs)
bubblesort(vectorbs)
insertionsort(vectorbs)
quicksort(vectorbs)
