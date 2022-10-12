``` js
combinciones(p1:list, p2: list){
    lista =[]                                                       
    r = []                                                     
    u = []
    for i = 0 to int(p2[0] - p1[0]){
      r.add("r")
      lista.add("r")
    }
    for i = 0 to int(p2[1] - p1[1]){
      r.add("u")
      lista.add("u")
    }

    numerador = factorial( lenght(r) + lenght(u) )
    denomindor = factorial( lenght(r) * factorial(lenght(u)) )
    numeroCombinaciones = int( numerador / denominador )

    return numeroCombinaciones
}


```