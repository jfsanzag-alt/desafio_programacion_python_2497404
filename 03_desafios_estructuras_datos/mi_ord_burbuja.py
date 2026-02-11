# Ordenamiento burbuja con recursividad
def ordena_burbuja_rec(lista):
    i = 0
    while i < len(lista)-1:
        if lista[i] > lista[i+1]:
            temp = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = temp
            print(i)
            ordena_burbuja_rec(lista)
        i += 1

    return lista

#Ordenamiento burbuja sin recursividad
def ordena_burbuja(lista):
    for j in range(0, len(lista)):
        print(j)
        for i in range(0, len(lista) - j - 1):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                print(lista)

    return(lista)

lista = [5, 6, 13, 2, 9, 1, 17]
print(lista)
#print(ordena_burbuja_rec(lista))
print(ordena_burbuja(lista))
#print(ordena_burbuja_rec([3,8,4,1,2]))
