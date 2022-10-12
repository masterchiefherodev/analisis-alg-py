``` js
insertion(lista : list){
  for i = 1 to lenght(lista){
    elemento = lista[i]
    j = i - 1
    while( j >= 0 and elemento < lista[j] ){
      lista[j + 1] = lista[j]
      j = j - 1
    }
    lista[j + 1] = elemento
    print("El vector ordenado es: " + lista)
  }
}
```