#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 4-bis "producto matricial" del Módulo 4 (esqueleto inicial)

m = [[1, 2], [3, 4], [5, 6]]  # matriz 3*2 (filas*columnas)
n = [[5, 10, 15, 0], [0, 0, 20, 0]]  # matriz 2*4

# m = [[1, 2, 6], [3, 4, 6]]  # matriz 2*3 (filas*columnas)
# n = [[5, 10, 15, 0, 20], [0, 0, 20, 0, 10], [10, 0, 10, 0, 30]]  # matriz 3*5


# Filas y columnas del resultado
a = len(m)  # filas de m
filas = a
d = len(n[0])  # columnas de n
columnas = d

b = len(m[0])  # columnas de m
c = len(n)  # filas de n

if b != c:
    print("Error, no calculable")
    exit(1)  # termina por completo el programa, indicando error 1

# Opcional: hacer más comprobaciones (todas las filas iguales, etc.)
# antes de continuar (...)


# Como ejemplo, se empieza por calcular r[0][0], a lo que le llamo x
x = 0
for variable in {}:  # MODIFICAR ESTO !!!
    for variable in {}:  # MODIFICAR ESTO !!!
        # Resultado para una celda dada
        for i in range(b):
            sumando = m[0][i] * n[i][0]
            print(f"Iteración {i}: sumando vale {sumando}")
            x = x + sumando

print(x)
