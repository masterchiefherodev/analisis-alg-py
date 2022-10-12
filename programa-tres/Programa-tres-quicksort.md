``` js
quicksort(lista : list) {
  particionado(lista : list){
    pivote = lista[0]
    izq = []
    der = []
    for i = 1 to lenght(lista){
      if(lista[i] < pivote){
        izq.add(lista[i])
      }else{
        der.add(lista[i])
      }
    }
    return izq, pivote, der
  }

  quickRecursivo(lista : list){
    if(lenght(lista) < 2){
      return lista
    }
    [izq, pivote, der] = particionado(lista)
    return quickRecursivo(izq) + [pivote] + quickRecursivo(der)
  }
  print("El vector ordenado es: " + quickRecursivo(lista : list))
}
```