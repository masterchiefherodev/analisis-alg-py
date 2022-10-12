from random import sample
# Importamos un Método de la biblioteca random para generar listas aleatorias

lista = list(range(100))  # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample
# (8 elementos aleatorios de la lista base)
vectorbs = sample(lista, 8)
print("El vector a ordenar es:", vectorbs)

# Complejidad O(n²)


def selection(lista: list):
    # Esta función ordenara el vector que le pases como argumento con el Método Selection Sort

    for i in range(len(lista)):
        # Empezados desde el inicio de la lista para acomodar cada elemento en su respectivo lugar
        # Econtrntramos el minimo elemento de los restantes sin ordenar
        minimo = i
        # Como ya se han acomodado los anteriores elementos y contamos en la variable minimo con el indice i, las iteraciones para buscar el minimo se harán a partir de [i+1] hasta el resto de la lista
        for j in range(i+1, len(lista)):
            if lista[minimo] > lista[j]:
                minimo = j
                # Acomodamos el elemento minimo encontrado con el lugar de la lista en el que vamos en la iteración [i], es decir en el lugar que le corresponde
        lista[i], lista[minimo] = lista[minimo], lista[i]
        # Repetimos el proceso hasta terminar
    print("El vector ordenado es (selección): ", lista)


selection(vectorbs)
