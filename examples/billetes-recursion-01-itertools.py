#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 7 (opcional) "billetes" del Módulo 5 (funciones)

# Solución ALTERNATIVA, SIN recursión (como se haría probablem. en un caso real),
# usando iteradores avanzados del módulo itertools (ver Módulo 5, casi al final...)

# Adaptado a partir de: https://realpython.com/python-itertools/#et-tu-brute-force
# © 2012–2020 Real Python
#   NOTA: código en GitHub:
#   https://github.com/realpython/materials/tree/master/itertools-in-python3


import itertools as it

# Valores de entrada
change_for = 100
bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5]

result = set()  # para descartar repetidos!
numcomb = 0

# ir probando con combinaciones de DIFERENTES longitudes...
for n in range(1, len(bills) + 1):
    # itertools.combinations (ver su ayuda) nos da justo lo necesario!
    for combination in it.combinations(bills, n):
        numcomb = numcomb + 1
        if sum(combination) == change_for:
            # si era una comb. correcta (suma lo deseado), ordenarla
            # para unificar las que sean "equivalentes" por tener
            # varios bill. del mismo valor; o sea, el orden no importa
            comb = sorted(combination, reverse=True)
            # sorted devuelve una lista, y para el set necesitamos tupla,
            # por lo que la convertimos (aunque se haría autom. en este caso)
            result.add(tuple(comb))
# NOTA: observar que con 10 billetes, salen 2 ** 10 combinaciones (menos una,
# porque no es válido el caso de 0 billetes elegidos), o sea, 1023. Era lo
# esperable porque al final cada billete tiene 2 opciones: estar o no...
print(numcomb, "combinations found")
print(len(result), "valid results:")
print(result)
print()


# Resultado que tiene que salir para esos valores:
# {(20, 20, 20, 10, 10, 10, 10), (20, 20, 10, 10, 10, 10, 10, 5, 5), (20, 20, 20, 10, 10, 10, 5, 5)}
