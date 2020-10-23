#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución 1 para el Ejercicio 4 "buscar repetidos" del Módulo 3

cadena = input("Escribe una lista de palabras separadas por espacios: ")
subcadena = ""

for i in cadena.split():  # recorrer cada una de las palabras de "cadena" con la variable i
    if subcadena.find(i) >= 0:  # si la palabra actual está entre las anteriores...
        print(f"'{i}' está repetida")  # entonces es que está repetida (caso que nos piden -> print)
    subcadena = subcadena + " " + i  # guardar la palabra actual en la "lista" de anteriores

# NOTA: si una palabra es una "subpalabra" de una anterior, también la detectará!
