lista = [27, 6, -50, 21, -3, 14, 16, -8, 42, 33, -21, 9, ]


def maxSumaIF(s: list):
    # Suma con dos if
    # [ini = inicio, fin = fin] de la sucecion de la lista que contiene la suma maxima posible
    ini, fin, tmp = 0, 0, 0
    max = 0
    # Suma de sucesión de elementos
    suma = 0
    for i in range(len(s)):
        if (suma + s[i]) > 0:
            # Si la suma es un número positivo la asigna
            suma = suma + s[i]
        else:
            # Si la suma es un número negativo se recorre el indice tmp (que mas tarde se asignará a inicio si se logra la suma maxima), y la suma se resetea igualandola a 0
            tmp = i + 1
            suma = 0
        if suma > max:
            # Si el acumulado de la suma es mayor al maximo anterior se asigna el maximo = suma, y se actualiza el valor tmp a inicio (pues es cuando se reseteo la suma, por tanto el principio de esta)  y el fin = a la interacion (posición actual).
            ini, fin = tmp, i
            max = suma
    # Devualve el maximo y de la lista original el segmento que conforma la suma maxima
    return max, s[ini: fin + 1]


def maxSumaFOR(s: list):
    # Suma con dos for
    suma = 0
    listaSuma = []
    # Se utilizan dos for para crear todos los posibles subconjuntos que pertenecen al conjunto s (original pasado como parametro)
    for i in range((len(s)) + 1):
        for j in range((len(s)) + 1):
            # Si el subconjunto no es vacio
            if s[i:j] != []:
                # Se asigna el valor de la suma de los elementos del subconjunto a tmp
                tmp = sum(s[i:j])
                # Si dicha suma es mayor a la suma mayor se asigna
                if suma < tmp:
                    suma = tmp
                    # Se asigna de igual manera el subconjunto con la suma maxima de elementos a la variable listaSuma para ser devuelta mas tarde
                    listaSuma = s[i:j]
    # Se repite para todos los subconjuntos y se obtienen las variables
    # Suma = con la suma maxima
    # listaSuma = con la lista o subconjunto de elementos que conforman la suma maxim
    return suma, listaSuma


print("Suma con con dos if:  ", maxSumaIF(lista))
print("Suma con con dos for: ", maxSumaFOR(lista))
