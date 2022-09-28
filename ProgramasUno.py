lista = [27, 6, -50, 21, -3, 14, 16, -8, 42, 33, -21, 9]


def maxSumaIF(s: list):
    # Suma con dos if
    ini, fin, tmp = 0, 0, 0
    max = 0
    suma = 0
    for i in range(len(s)):
        if (suma + s[i]) > 0:
            suma = suma + s[i]
        else:
            tmp = i + 1
            suma = 0
        if suma > max:
            ini, fin = tmp, i
            max = suma
    return max, s[ini: fin + 1]


def maxSumaFOR(s: list):
    # Suma con dos for
    suma = 0
    listaSuma = []
    for i in range((len(s)) + 1):
        for j in range((len(s)) + 1):
            if s[i:j] != []:
                tmp = sum(s[i:j])
                if suma < tmp:
                    suma = tmp
                    listaSuma = s[i:j]
    return suma, listaSuma


print("Suma con con dos if:  ", maxSumaIF(lista))
print("Suma con con dos for: ", maxSumaFOR(lista))
