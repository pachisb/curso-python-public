#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Soluciones para el Ejercicio 1-bis "bucles sencillos" del Módulo 4


# PARTE 1: Escribir los números del 1 al 10
print("1 2 3 4 5 6 7 8 9 10")
print()


# PARTE 2: Escribir los números desde x (entero) a y (entero)
# siendo x e y variables numéricas ya dadas

x = 5
y = 9
for i in range(x, y+1):
    print(i)
print()


# PARTE 3: Escribir los números impares desde x a y (enteros)
# siendo x e y variables numéricas ya dadas

x = 6
y = 19

i = x
FIN = y
while i <= FIN:
    if i % 2 == 0:
        print(i)
    i = i + 1
print()


# PARTE 4: Escribir cada una de las letras de una cadena s (str)
# en una línea separada

s = "hola y tal"
for i in s:
    print(i)
