def parentesis_balanceados(cadena):
    
    num_par_de = cadena.count(")")
    num_par_iz = cadena.count("(")
    print(num_par_iz, num_par_de)

    return num_par_iz == num_par_de

print(parentesis_balanceados("(()())()"))  #true
print(parentesis_balanceados("() (())) ()")) #false

# No detecto el caso de apertura incorrecta ")("