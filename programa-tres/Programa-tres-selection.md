```js
selection(lista : list){
  for i to lenght(lista){
    minimo = i
    for j = (i + 1) to lenght(lista){
      if(lista[minimo] > lista[j]){
        minimo = j
      }
    }
    tmp = lista[i]
    lista[i] = lista[minimo]
    lista[j] = tmp
  }
  print("El vector ordenado es: " + lista)
}

```