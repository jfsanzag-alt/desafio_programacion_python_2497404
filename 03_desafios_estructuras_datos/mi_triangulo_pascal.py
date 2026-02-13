def triangulo_pascal(fila):
    #Inicio retorno
    tri_pascal = []
    #      1              
    #     1 1             
    #    1 2 1
    #   1 3 3 1
    #  1 4 6 4 1
    # 1 5 10 10 5 1

    # Inicio tri_pascal
    tri_pascal.append([1])
    if fila == 1:
        return tri_pascal
    
    tri_pascal.append([1,1])
    if fila == 2:
        return tri_pascal

    # Limite para iterar en filas
    limit_iter_filas = fila
    for i in range (2, limit_iter_filas):
        len_fila_ant = len(tri_pascal[i-1])
        fila_anterior = tri_pascal[i-1]
        lista_fila = []

        for j in range (0, len_fila_ant):
            if j == 0:
                lista_fila.append(fila_anterior[j])
            else:
                suma = fila_anterior[j] + fila_anterior[j-1]
                lista_fila.append(suma)

            if j == len_fila_ant - 1:
                lista_fila.append(fila_anterior[j])
                tri_pascal.append(lista_fila)

    return tri_pascal

for k in range(1, 10):
    print(f"triangulo de pascal {k}: {triangulo_pascal(k)}")
