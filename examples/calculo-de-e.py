#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 1 bis "cálculo de e" del Módulo 3

# Se usa la fórmula: e ^ x = ∑ (n=0 hasta ∞) x/(n!)
#  ... suponiendo x = 1 idealmente (más sencillo)
# Es decir, calcular: 1/0! + 1/1! + 1/2! + 1/3! + 1/4! + ...

# Valor de e aprox.
n = 20  # numero de iteraciones
i = 0  # contador de iteración actual
e = 0.0  # valor final de e (resultado), para ir acumulando
fact = 1  # valor del factorial de i en cada iteración

while i < n:
    if i > 0:  # evitar el caso especial del factorial de 0 (que lo tenemos ya de inicio: fact = 1)
        fact *= i  # nota: podríamos calcular el factorial de i cada vez, pero esto es una optimización
    e += 1.0 / fact
    i += 1
print(f"Solución alcanzada (en {i} iteraciones):")
print(e)


# Lo siguiente, sólo como comprobación...

import math

print("Valores según el módulo math:")
print(math.exp(1.0))
print(math.e)
