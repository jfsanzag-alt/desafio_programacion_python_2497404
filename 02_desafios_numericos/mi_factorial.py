def factorial_ciclo(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i

    return fact

def factorial_recursivo(num):
    if num <= 1:
        return num
    
    return num * factorial_recursivo(num-1)

for i in range(1, 10):
    fact = factorial_ciclo(i)
    print(f"Factorial de {i}: {fact}")

print(factorial_recursivo(5))