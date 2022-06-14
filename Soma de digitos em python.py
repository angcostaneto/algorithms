def somaNumero(maxDigit):
  listaNumeros = []
  for numero in range (1000, 7770):
    # verifica o ultimo digito
    ultimoDigito = int(repr(numero)[-1])
    if (ultimoDigito > maxDigit):
      continue
    
    soma = 0
    for valor in str(numero):
      soma += int(valor)
      if soma == 21:
        listaNumeros.append(numero)
        continue

  return listaNumeros
    
print(somaNumero(6))