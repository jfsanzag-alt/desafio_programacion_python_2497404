def es_num_primo(num):
    if num <= 1:
        return False
    
    i = 2
    while (i <= (num - 1)): 
        if (num % i) == 0:
            return False
        i += 1
    return True

lista_primos=[]
i = 0
#while i < 20:
for i in range(0,20):
    es_primo = (es_num_primo(i))
    print(f"{i} es primo: {es_primo}")
    if es_primo:
        lista_primos.append(i)

print(lista_primos)