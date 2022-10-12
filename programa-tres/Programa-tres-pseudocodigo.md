``` js
bubble(lista : list){
  for i = 0 to lenght(lista){
    for j = 0 to lenght(lista){
      if(lista[j] > lista[i]){
        tmp = lista[i]
        lista[i] = lista[j]
        lista[j] = tmp
      }
    }
  }
  print("El vector ordenado es: " + lista)
}
```