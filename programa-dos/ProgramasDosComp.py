import math

p1 = [2, 1]
p2 = [7, 4]
result = []


def combinaciones(p1: list, p2: list, res: list):
    lista = []                                                          # 1
    r = []                                                              # 1
    u = []                                                              # 1
    for i in range(p2[0] - p1[0]):                                      # n
        r.append("r")                                                   # n
        lista.append("r")                                               # n
    for i in range(p2[1] - p1[1]):                                      # n
        u.append("u")                                                   # n
        lista.append("u")                                               # n

    numerador = math.factorial((len(r) + len(u)))                       # 1
    denominador = math.factorial(len(r)) * math.factorial(len(u))       # 1
    numeroCombinaciones = int(numerador / denominador)                  # 1

    for i in range(numeroCombinaciones):                                # n
        pass                                                            # n
    return (numeroCombinaciones)
    # 8n + 6 = O(n) ∴ Es una función lineal


print("El número de combinaciones posibles es: ", combinaciones(p1, p2, result))
