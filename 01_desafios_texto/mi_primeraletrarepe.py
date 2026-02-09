def mi_primera_letra_repe(texto):
  texto_minuscula = texto.lower()
  texto_sin_espacio = texto_minuscula.replace(" ", "")

  for letra in texto_sin_espacio:
    contador = texto_sin_espacio.count(letra)
    if contador > 1:
      return letra
  
  return None
    
texto ="Texto tecnico"
print(texto)
print(mi_primera_letra_repe(texto))
