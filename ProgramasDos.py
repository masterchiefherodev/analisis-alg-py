import math


p1 = [2, 1]
p2 = [7, 4]
result = []


def comb(p1: list, p2: list, res: list):
    # p1 : punto 1, p2: punto dos, res : lista resultante
    lista = []
    # Lista con los movimientos hacia la derecha
    r = []
    # Lista con los movimientos hacia arriba
    u = []
    # Se llena la lista con el número de r
    for i in range(p2[0] - p1[0]):
        r.append("r")
        lista.append("r")
    # Se llena la lista con el número de u
    for i in range(p2[1] - p1[1]):
        u.append("u")
        lista.append("u")

    # Se obtienen las combinaciones totales
    numerador = math.factorial((len(r) + len(u)))
    denominador = math.factorial(len(r)) * math.factorial(len(u))
    numeroCombinaciones = int(numerador / denominador)

    # Se lena la lista con las combiaciones posibles TODO
    for i in range(numeroCombinaciones):
        pass
    return (numeroCombinaciones)


print("El número de combinaciones posibles es: ", comb(p1, p2, result))
