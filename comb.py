import itertools
import math

posiciones = ["u", "u", "u", "u", "u", "r", "r", "r"]

# Codigo que factoriza, se usará el de la libreria math


def factorialRecursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorialRecursivo(n - 1)


def combinaciones(l):
    listaPermutada = []
    permutacion = list(itertools.permutations(l))
    for i in permutacion:
        if i not in listaPermutada:
            listaPermutada.append(i)
    return listaPermutada


p1 = [2, 1]
p2 = [7, 4]
result = []


def comb(p1: list, p2: list, res: list):
    # Variables
    lista = []
    r = []
    u = []
    listaCombinaciones = []
    # Se llena el numero de r
    for i in range(p2[0] - p1[0]):
        r.append("r")
        lista.append("r")
    # Se llena el numero de u
    for i in range(p2[1] - p1[1]):
        u.append("u")
        lista.append("u")
    # Se obtienen las combinaciones totales
    numerador = math.factorial((len(r) + len(u)))
    denominador = math.factorial(len(r)) * math.factorial(len(u))
    numeroCombinaciones = int(numerador / denominador)
    # Se lena la lista con las combiaciones posibles
    for i in range(numeroCombinaciones):
        pass
    return (numeroCombinaciones, res)


print("El número de combinaciones posibles es: ", comb(p1, p2, result)[0])
# print(combinaciones(posiciones))
