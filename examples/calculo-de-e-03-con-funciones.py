#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 1 bis "cálculo de e" del Módulo 3 (usando funciones)

# Se usa la fórmula: e ^ x = ∑ (n=0 hasta ∞) x/(n!)
#  ... suponiendo x = 1 idealmente (más sencillo)
# Es decir, calcular: 1/0! + 1/1! + 1/2! + 1/3! + 1/4! + ...

# Necesitamos/usaremos una función auxiliar para el cálculo del factorial
def factorial(n):
    result = 1
    i = 1
    while i <= n:
        result = result * i
        i = i + 1
    return result


# Valor de e aprox.
n = 10  # numero de iteraciones
e = 0.0  # valor final de e (resultado), para ir acumulando

for i in range(n):  # desde 0 hasta n-1 inclusive (n iteraciones)
    e = e + 1.0 / factorial(i)

print(f"Solución alcanzada (en {n} iteraciones):")
print(e)


# Lo siguiente, sólo como comprobación...

import math

print("Valor según el módulo math:")
print(math.e)
