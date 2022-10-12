``` js
maxSumaIF(s: list){
  ini = 0
  fin = 0
  tmp = 0
  suma = 0
  for i = 0 to lenght(s){
    if(suma + s[i] > 0){
      suma = suma + s[i]
    }else{
      tmp = i +1
      suma = 0
    }
    if(suma > max){
      ini = tmp
      fin = i
      max = suma
    }
  }
  return max, s[ini to (fin + i)]
}
```