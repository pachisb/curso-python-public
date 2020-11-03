#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 1 "media y suma" del Módulo 3 (con bucles while)

sum = 0
cuenta = 0

num = input("Dame el primer número (o nada o 'fin' para terminar): ")

while num != "fin" and num != "":
    sum = sum + float(num)
    cuenta = cuenta + 1
    num = input("Dame el siguiente número (o nada o 'fin' para terminar): ")


# Escribir el resultado (si tiene sentido)
if cuenta > 0:
    media = sum / cuenta
    print(f"La suma es", sum, "y la media es", media)
