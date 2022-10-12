``` js
maxSumaFOR(s : list){
  suma = 0
  listaSuma = []
  for i = 0 to lenght(s){
    for j = 0 to lenght(s){
      if(s[i to j] != []){
        tmp = suma(s[i to j])
        if(suma < tmp){
          suma = tmp
          listaSuma = s[i to j]
        }
      }
    }
  }
  return suma, listaSuma
}
```