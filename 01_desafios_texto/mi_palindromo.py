def es_palindromo(texto):
  textominuscula = texto.lower()
  textosinespacio = textominuscula.replace(" ", "")

  print(textosinespacio[::-1])

  return (textosinespacio == textosinespacio[::-1])

'''
  i = len(textosinespacio)
  for letra in textosinespacio:
    i -= 1
    textogirado += textosinespacio[i]

  return (textosinespacio == textogirado)
'''

#frase = "Anita laVa la Tina"
frase = "Mi frase es MI frase"

if es_palindromo(frase):
  print("Es palindromo")
else:
  print("No es palindromo")
