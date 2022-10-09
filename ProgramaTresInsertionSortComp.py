import datetime
from random import sample

lista = list(range(100))

vectorbs = sample(lista, 8)
print("El vector a ordenar es:", vectorbs)

# Complejidad O(n²)


def insertion(lista: list):
    for i in range(1, len(lista)):                              # n
        elemento = lista[i]                                     # n
        j = i-1                                                 # n
        while j >= 0 and elemento < lista[j]:                   # n * n = n²
            lista[j+1] = lista[j]                               # n * n = n²
            j -= 1                                              # n * n = n²
        lista[j+1] = elemento                                   # n
    print("El vector ordenado es (insersión): ", lista)         # 1
# 3n² + 4n + 1 = O(n²) ∴ Es una función cuadrática


before = datetime.datetime.now()
insertion(vectorbs)
after = datetime.datetime.now()
print("Timempo: ", (after - before))
