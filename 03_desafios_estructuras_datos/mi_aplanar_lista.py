def aplanar_lista(lista):
    lista_plana = []

    for elem in lista:
        if isinstance(elem, list): #Mas profesional. elem es lista y se comporta como lista
        #if type(elem) == list: #elem es de tipo lista
            lista_plana.extend(elem)
        else:
            lista_plana.append(elem)

    return lista_plana


lista_1 = [1, 2, [1, 2, 3], 3, 5, 7]
lista_2 = [1, True, "casa", ["Pedro", False, "Luis", 2], 1, "Jaime"]

print(aplanar_lista(lista_1))
print(aplanar_lista(lista_2))