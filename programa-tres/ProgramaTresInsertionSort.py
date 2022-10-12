from random import sample
# Importamos un Método de la biblioteca random para generar listas aleatorias

lista = list(range(100))  # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample
# (8 elementos aleatorios de la lista base)
vectorbs = sample(lista, 8)
print("El vector a ordenar es:", vectorbs)

# Complejidad O(n²)


def insertion(lista: list):
    # Esta función ordenara la lista que le pases como argumento con el Método Insertion Sort

    # Recorremos la lista de 1 hasta el largo total
    for i in range(1, len(lista)):

        elemento = lista[i]
        # Se va a ir recorriendo desde un indice a la izquierda puesto que esos elementos ya esta ordenados (los elementos a la izquierda del elemento en i)
        j = i-1

        while j >= 0 and elemento < lista[j]:
            # Mientras que el indice de la lista sea mayor o igual a 0, y el "elemento" sea mas pequeño que el elemento de la lista en j los elementos de la ista se han de recorrer un indice a la derecha. Con esto se consigue colocar el elemento en su lugar
            lista[j+1] = lista[j]
            j -= 1
        # Coloca el elemento en su posicion
        lista[j+1] = elemento
    print("El vector ordenado es (insersión): ", lista)


insertion(vectorbs)
