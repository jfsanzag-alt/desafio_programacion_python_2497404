def num_triangular(fila):
    num_tri = 0
    for num in range (1, fila+1):
        num_tri += num

    return num_tri

#print(num_triangular(4))
for i in range (1, 11):
    print(f"num {i}: num_triangular: {num_triangular(i)}")
