def parentesis_balanceados(cadena):
    
    # No detecto el caso de apertura incorrecta ")("
    '''
    num_par_de = cadena.count(")")
    num_par_iz = cadena.count("(")
    print(num_par_iz, num_par_de)

    return num_par_iz == num_par_de
    '''

    #Algoritmo correcto
    i = 0
    num_par = 0
    while i < len(cadena):
        if cadena[i] == "(":
            num_par += 1
        elif cadena[i] == ")":
            num_par -= 1
            if num_par < 0:
                return False
        i += 1

    return (num_par == 0)


print(parentesis_balanceados("(()())()"))  #true
print(parentesis_balanceados("() (())) ()")) #false

print(parentesis_balanceados("((()))()"))  #true
print(parentesis_balanceados(")(()"))  #false
print(parentesis_balanceados("(()"))  #false
