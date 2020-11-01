#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 4-bis "producto matricial" del Módulo 4 (COMPLETA)

m = [[1,2],[3,4],[5,6]]  # matriz 3*2 (filas*columnas)
n = [[5,10,15,0],[0,0,20,0]]  # matriz 2*4

# m = [[1,2,6],[3,4,6]]  # matriz 2*3 (filas*columnas)
# n = [[5,10,15,0,20],[0,0,20,0,10],[10,0,10,0,30]]  # matriz 3*5


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


# La matriz resultado (a*d) será r
r = []
for k in range(filas):  # a (==filas) iteraciones
    # l es una fila de resultados (una de las de la matriz final)
    l = []
    for j in range(columnas):  # d (==columnas) iteraciones
        # Calcular el elemento r[k][j], al que llamo x
        x = 0
        for i in range(b):
            sumando = m[k][i] * n[i][j]
            # print(f"Iteracion {i}: sumando vale {sumando}")
            x = x + sumando
        l.append(x)  # Agregar el resultado de esta "celda" a l
    # Agregar la fila de resultados al resultado final r
    r.append(l)

# Opcional: imprimir el resultado más "legible":
cadena = str(r)  # esto tendrá el aspecto "[[.... ], [...]]"
print(cadena.replace("], [", "],\n["))
