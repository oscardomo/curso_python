# Calcular el factorial de un número dado def factorial(n): Si n es 0 o 1, devolver 1 (caso base) En otro caso, devolver n * factorial(n-1)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))