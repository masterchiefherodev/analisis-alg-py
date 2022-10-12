import datetime
from random import sample

lista = list(range(100))

vectorbs = sample(lista, 8)
print("El vector a ordenar es:", vectorbs)

# Complejidad O(n²)


def selection(lista: list):
    for i in range(len(lista)):                             # n
        minimo = i                                          # n
        for j in range(i+1, len(lista)):                    # n * n = n²
            if lista[minimo] > lista[j]:                    # n * n = n²
                minimo = j                                  # n * n = n²
        lista[i], lista[minimo] = lista[minimo], lista[i]   # n
    print("El vector ordenado es (selección): ", lista)     # 1
# 3n² + 3n + 1 = O(n²) ∴ Es una función cuadrática


before = datetime.datetime.now()
selection(vectorbs)
after = datetime.datetime.now()
print("Timempo: ", (after - before))
