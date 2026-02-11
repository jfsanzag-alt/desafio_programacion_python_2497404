def lista_duplicados(lista):
    lista_dup = []

    '''
    for elem in lista:
        print(f"{elem}: {lista_dup.count(elem)}")
        if lista.count(elem) > 1 and lista_dup.count(elem) == 0:
            lista_dup.append(elem)
    '''

    for elem in lista:
        # Contamos cuántas veces aparece el elemento con el MISMO VALOR Y TIPO
        conteo_real = sum(1 for x in lista if x == elem and type(x) == type(elem))
        # Contamos si ya lo metimos en la lista de resultados con el MISMO TIPO
        ya_esta = sum(1 for x in lista_dup if x == elem and type(x) == type(elem))

        if conteo_real > 1 and ya_esta == 0:
            lista_dup.append(elem)

    return lista_dup

def encontrar_duplicados_eficiente(lista):
    conteo = {}
    duplicados = []

    for elem in lista:
        # Creamos una "llave" única que combina valor y tipo
        # Ejemplo: (1, <class 'int'>) es distinto a (True, <class 'bool'>)
        llave = (elem, type(elem))
        
        # Vamos contando las apariciones
        conteo[llave] = conteo.get(llave, 0) + 1
        
        # Si es la segunda vez que lo vemos, lo mandamos a la lista de duplicados
        if conteo[llave] == 2:
            duplicados.append(elem)
            
    return duplicados

# Esta no funciona con booleanos
def encontrar_duplicados(lista):

    elementos_lista = []
    duplicados = []

    for elemento in lista:

        if elemento in elementos_lista:
            duplicados.append(elemento)
        else:
            elementos_lista.append(elemento)

    return duplicados

lista = [1, 2, 3, 1, 4, 2, 6, 7]
lista_2 = [1, "casa", "barco", True, 2, 1, False, True, "casa"]

#print(lista_duplicados(lista))
#print(lista_duplicados(lista_2))
print(encontrar_duplicados_eficiente(lista))
print(encontrar_duplicados_eficiente(lista_2))
#print(encontrar_duplicados(lista))
#print(encontrar_duplicados(lista_2))
