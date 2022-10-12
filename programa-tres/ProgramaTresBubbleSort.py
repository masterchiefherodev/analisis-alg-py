from random import sample
# Importamos un Método de la biblioteca random para generar listas aleatorias

lista = list(range(100))  # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample
# (8 elementos aleatorios de la lista base)
vectorbs = sample(lista, 8)
print("El vector a ordenar es:", vectorbs)

# Complejidad O(n²)


def bubble(lista: list):
    # Esta función ordenara el vector que le pases como argumento con el Método de Bubble Sort
    for i in range(len(lista)):
      # Se recorre la lista para comparar cada uno de los elementos que se encuentran en el indice i
        for j in range(len(lista)):
            # Se compara con cada elemento en j
            if lista[j] > lista[i]:
                # Si el elemento en j es mayor al elemento en i se intercambian
                lista[j], lista[i] = lista[i], lista[j]
            # Se usa doble asignación para realizar el cambio
    print("EL vector ordenado es (bubble):", lista)


bubble(vectorbs)
