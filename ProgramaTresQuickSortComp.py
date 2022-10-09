import datetime
from random import sample

lista = list(range(100))

vectorbs = sample(lista, 8)
print("El vector a ordenar es:", vectorbs)

# Complejidad O(nLog(n))


def quickSort(lista: list):

    def particionado(lista: list):
        pivote = lista[0]                   # 1
        izq = []                            # 1
        der = []                            # 1
        for i in range(1, len(lista)):      # n
            if(lista[i] < pivote):          # n
                izq.append(lista[i])        # n
            else:
                der.append(lista[i])        # n
        return izq, pivote, der

    def quickRecursivo(lista: list):
        if(len(lista) < 2):                                         # 1
            return lista
        izq, pivote, der = particionado(lista)                      # 1
        return quickRecursivo(izq) + [pivote] + quickRecursivo(der)  # n Log(n)
    print("El vector ordenado es (quicksort): ", quickRecursivo(vectorbs))  # 1
# nLog(n) + 4n + 6 = O(nLog(n)) ∴ Es una función Logaritmica


before = datetime.datetime.now()
quickSort(vectorbs)
after = datetime.datetime.now()
print("Timempo: ", (after - before))
