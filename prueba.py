"""
Calcula el factorial de un número (ejemplo: factorial(5) = 120).
"""


def factorial(n):
    """
    Calcula el factorial de n (n!).

    El factorial de 0 y 1 es 1. Para n > 1: n! = n * (n-1)!.

    Args:
        n: Entero no negativo.

    Returns:
        El factorial de n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))