import datetime


lista = [27, 6, -50, 21, -3, 14, 16, -8, 42, 33, -21, 9]


def maxSumaIF(s: list):
    ini, fin, tmp = 0, 0, 0       # 1
    max = 0                       # 1
    suma = 0                      # 1
    for i in range(len(s)):       # n
        if (suma + s[i]) > 0:     # n
            suma = suma + s[i]    # n
        else:                     # n
            tmp = i + 1           # n
            suma = 0              # n
        if suma > max:            # n
            ini, fin = tmp, i     # n
            max = suma            # n
    return max, s[ini: fin + 1]   # 9n + 3 = O(n) ∴ Es una función lineal


before = datetime.datetime.now()
print("Suma con con dos if:  ", maxSumaIF(lista))
after = datetime.datetime.now()
print("Timempo: ", (after - before))


def maxSumaFOR(s: list):
    suma = 0                              # 1
    listaSuma = []                        # 1
    for i in range((len(s)) + 1):         # n
        for j in range((len(s)) + 1):     # n * n = n²
            if s[i:j] != []:              # n * n = n²
                tmp = sum(s[i:j])         # n * n = n²
                if suma < tmp:            # n * n = n²
                    suma = tmp            # n * n = n²
                    listaSuma = s[i:j]    # n * n = n²
    return suma, listaSuma
    # 6n² + n + 2 = O(n²) ∴ Es una función cuadrática


before = datetime.datetime.now()
print("Suma con con dos for: ", maxSumaFOR(lista))
after = datetime.datetime.now()
print("Timempo: ", (after - before))
