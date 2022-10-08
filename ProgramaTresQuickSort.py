def quicksort(vectorbs, start=0, end=len(vectorbs) - 1):
    """Esta función ordenara el vector que le pases como argumento 
    con el Método Quick Sort"""

    def quick(vectorbs, start=0, end=len(vectorbs) - 1):

        if start >= end:
            return

        def particion(vectorbs, start=0, end=len(vectorbs) - 1):
            pivot = vectorbs[start]
            menor = start + 1
            mayor = end

            while True:
                # Si el valor actual es mayor que el pivot
                # está en el lugar correcto (lado derecho del pivot) y podemos
                # movernos hacia la izquierda, al siguiente elemento.
                # También debemos asegurarnos de no haber superado el puntero bajo, ya que indica
                # que ya hemos movido todos los elementos a su lado correcto del pivot
                while menor <= mayor and vectorbs[mayor] >= pivot:
                    mayor = mayor - 1

                # Proceso opuesto al anterior
                while menor <= mayor and vectorbs[menor] <= pivot:
                    menor = menor + 1

                # Encontramos un valor sea mayor o menor y que este fuera del arreglo
                # ó menor es más grande que mayor, en cuyo caso salimos del ciclo
                if menor <= mayor:
                    vectorbs[menor], vectorbs[mayor] = vectorbs[mayor], vectorbs[menor]
                    # Continua el bucle
                else:
                    # Salimos del bucle
                    break

            vectorbs[start], vectorbs[mayor] = vectorbs[mayor], vectorbs[start]

            return mayor

        p = particion(vectorbs, start, end)
        quick(vectorbs, start, p-1)
        quick(vectorbs, p+1, end)

    quick(vectorbs)
    print("El vector ordenado es (quicksort):", vectorbs)