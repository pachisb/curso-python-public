#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 1 bis "cálculo de e" del Módulo 3

# Se usa la fórmula: e ^ x = ∑ (n=0 hasta ∞) x/(n!)
#  ... suponiendo x = 1 idealmente (más sencillo)
# Es decir, calcular: 1/0! + 1/1! + 1/2! + 1/3! + 1/4! + ...

# Opcional: número de iteraciones tal que la precisión se alcance
prec = 0
while prec <= 0:
    f = float(input("Dame un número de decimales de precisión: "))
    if f > 0:
        prec = 0.1 ** ( f )
print(prec)

# Valor de e aprox.
n = 100  # numero máximo de iteraciones (como límite superior, por si acaso)
i = 0  # contador de iteración actual
e = 0.0  # valor final de e (resultado), para ir acumulando
ult_error = 99  # opcional: valor de e de la iteración actual menos el de la anterior, para lo de la precisión
fact = 1  # valor del factorial de i en cada iteración

while i < n and prec < ult_error:  # sin la parte opcional, sería simplemente quitar la segunda parte: and ...
    fact *= i or 1  # expresión breve (con or) para evitar que valga 0
    e_ant = e
    e += 1.0 / fact
    ult_error = e - e_ant
    i += 1
print(f"Solución alcanzada (en {i} iteraciones):")
print(e)


# Lo siguiente, sólo como comprobación...

import math

print("Valores según el módulo math:")
print(math.exp(1.0))
print(math.e)
