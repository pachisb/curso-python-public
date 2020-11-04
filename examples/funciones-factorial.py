#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ejemplo de funciones y recursión para el Módulo 5


def factorial(n):
    """Cálculo "estándar" (bucles) del factorial de un número"""
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


# Alternativa equivalente von while, vista en clase
# def factorial(n):
#     result = 1
#     i = 2
#     while i <= n:
#         result = result * i
#         i = i + 1
#     return resul

print(factorial(5))
print(factorial(10))
print(factorial(2000))


def factorial_recursivo(n):
    """Cálculo del factorial de forma recursiva"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial_recursivo(5))
print(factorial_recursivo(10))
# print(factorial_recursivo(2000))  # NOTA: esto da error! ¿por qué?
