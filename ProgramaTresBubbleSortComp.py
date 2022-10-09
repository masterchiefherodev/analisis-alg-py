import datetime
from random import sample

lista = list(range(100))

vectorbs = sample(lista, 8)
print("El vector a ordenar es:", vectorbs)

# Complejidad O(n²)


def bubble(lista: list):
    for i in range(len(lista)):                             # n
        for j in range(len(lista)):                         # n * n = n²
            if lista[j] > lista[i]:                         # n * n = n²
                lista[j], lista[i] = lista[i], lista[j]     # n * n = n²
    print("EL vector ordenado es (bubble):", lista)         # 1
    # 3n² + n + 1 = O(n²) ∴ Es una función cuadrática


before = datetime.datetime.now()
bubble(vectorbs)
after = datetime.datetime.now()
print("Timempo: ", (after - before))
