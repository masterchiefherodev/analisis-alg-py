import math


def matrix(n: int, res: list):
    if n == 0:
        return [[]]
    else:
        m = matrix(n - 1, res)
    return [[i] + item for i in (0, 1) for item in m]


def combinaciones(p1: list, p2: list, res: list):
    # Se obtienen las combinaciones totales
    numerador = math.factorial(p2[0] - p1[0] + p2[1] - p1[1])
    denominador = math.factorial(p2[0] - p1[0]) * math.factorial(p2[1] - p1[1])
    numeroCombinaciones = int(numerador / denominador)
    cont = int(numerador / denominador)
    # Se generan las combinaciones
    return (numeroCombinaciones, res)


posiciones = ["u", "u", "u", "u", "u", "r", "r", "r"]
result = []


def listaReordenada(lista: list, res: list):
    for i in range(56):
        lista.append(lista[0])
        del lista[0]
        print(not (lista in res))
        if not (lista in res):
            res.append(lista)
    return res


listaReordenada(posiciones, result)
