#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio extra "producto matricial" del Módulo 5
# Es una mejora sobre lo anterior del Módulo 4, "refactorizando" el código en funciones


def calculos_inicio(m1, m2):
    a = len(m1)  # filas de m1
    b = len(m1[0])  # columnas de m1
    c = len(m2)  # filas de m2
    d = len(m2[0])  # columnas de m2

    errores = False
    if b != c:
        print("Error, no calculable por las dimensiones de las matrices")
        errores = True
    elif a == 0 or b == 0 or d == 0:
        print("Error, las matrices no pueden tener filas o columnas vacías")
        errores = True

    # Opcional: hacer más comprobaciones (todas las filas iguales)
    for fila in m1:
        if len(fila) != b:
            print("Error, las matrices no pueden tener filas de diferente tamaño")
            errores = True
    for fila in m2:
        if len(fila) != d:
            print("Error, las matrices no pueden tener filas de diferente tamaño")
            errores = True

    return errores, a, b, c, d


def producto_matricial(m1, m2, fil, col):
    b = len(m1[0])  # columnas de m1, también necesario aquí

    # La matriz resultado (a*d) será r
    r = []
    for k in range(fil):  # tantas iteraciones como filas
        # l es una fila de resultados (una de las de la matriz final)
        l = []
        for j in range(col):  # tantas iteraciones como col.
            # Calcular el elemento r[k][j], al que llamo x
            x = 0
            for i in range(b):
                sumando = m1[k][i] * m2[i][j]
                # print(f"Iteracion {i}: sumando vale {sumando}")
                x = x + sumando
            l.append(x)  # Agregar el resultado de esta "celda" a l
        # Agregar la fila de resultados al resultado final r
        r.append(l)

    return r


def print_matriz(m):
    # Imprimir el resultado más "legible":
    cadena = str(m)  # esto tendrá el aspecto "[[.... ], [...]]"
    # Esto sustituye algunos espacios por saltos de línea
    print(cadena.replace("], [", "],\n["))


# Inicio del programa principal

m = [[1, 2], [3, 4], [5, 6]]  # matriz 3*2 (filas*columnas)
n = [[5, 10, 15, 0], [0, 0, 20, 0]]  # matriz 2*4

# m = [[1, 2, 6], [3, 4, 6]]  # matriz 2*3 (filas*columnas)
# n = [[5, 10, 15, 0, 20], [0, 0, 20, 0, 10], [10, 0, 10, 0, 30]]  # matriz 3*5


# Filas y columnas del resultado
errores, a, b, c, d = calculos_inicio(m, n)
if errores:
    exit(1)  # termina por completo el programa, indicando error 1

filas = a
columnas = d

r = producto_matricial(m, n, filas, columnas)

# print(r)
# Opcional: imprimir el resultado más "legible":
print_matriz(r)
