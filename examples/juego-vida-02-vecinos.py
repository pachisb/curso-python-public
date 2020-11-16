#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 3 "juego de la vida (parte 1)" del Módulo 5 (COMPLETA)

FILAS = 0
COLUMNAS = 0
tablero_texto = """\
11100000000000000000000000000000000000000000000000000000000000000000000000000000
00000000110000000000000000011100000011100000000000000000000000000000000000000000
00000001001000000000000000000000010000000000000000000000000000000000000000000000
00000000110000000000000000000000010000000000000000000000000000000000000000000000
00000000000000000000000000000000010000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000110000000000000000000000000000000010000000000000000000000000000000
00000000000000110000000000000000000000000000001010000000000000000000000000000000
00000000000000001100000000000000000000000000000110000000000000000000000000000000
00000000000000001100000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000110000000000000000000000000000000
00000000000000000000000000000000000000000000001100000000000000000000000000000000
00000000000000000000000000000000000000000000000100000000000000000000000000000000
"""

def leer_tablero(tablero_cadena):
    """Convierte una cadena adecuada en una matriz, para operar mejor con ella"""
    i = 0
    l = []  # Una lista para ir generando una fila
    m = []  # La matriz resultado
    global FILAS, COLUMNAS
    for celda in tablero_cadena:
        if celda == '\n':
            if COLUMNAS == 0:
                COLUMNAS = len(l)
            elif COLUMNAS != len(l):
                print(f"Error en la fila {FILAS}, faltan o sobran datos!")
                exit(1)
            FILAS = FILAS + 1
            m.append(l)
            l = []
        else:
            # Por si acaso se usa algo distinto de 1's, lo aceptamos igual
            valor = 0 if celda == "0" else 1
            l.append(valor)

    return m


def print_tablero(m):
    """Escribe por pantalla la matriz m con formato de tablero de 0's y 1's"""
    print(str(m).replace(",", "").replace(" ", "").replace("[", "").replace("]","\n"))


def clear_screen():
    """Limpia la pantalla (en consola). Válido en Linux, Mac y Windows"""
    # NOTA: no sirve en modo interactivo, IPython, Jupyter notebook, etc.
    import os
    os.system('cls' if os.name=='nt' else 'clear')


# Comienzo del programa
m = leer_tablero(tablero_texto)
clear_screen()
print("Tablero inicial:")
print_tablero(m)


def num_vecinos(m, x, y):
    """Devuelve el número de vecinos de la celda m[y][x], como un valor de 0 a 8"""
    result = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != 0 or j != 0:  # no contar la celda en sí!
                if (x + i >= 0) and (x + i < COLUMNAS) and (y + j >= 0) and (y + j < FILAS):
                    result += m[y+j][x+i]
    return result

print(num_vecinos(m, 0, 0))
print(num_vecinos(m, 1, 0))
print(num_vecinos(m, 2, 0))
print(num_vecinos(m, 0, 1))
print(num_vecinos(m, 1, 1))
print(num_vecinos(m, 2, 1))
