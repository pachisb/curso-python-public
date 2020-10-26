#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución USANDO LISTAS para el Ejercicio 4 "buscar repetidos" del Módulo 3

cadena = input("Escribe una lista de palabras separadas por espacios: ")
lista = cadena.split()
# print("LISTA:", lista)  # para depurar, opcional, quitar en la versión final
sublista_previas = []
soluciones = []

for palabra in lista:  # recorrer cada una de las palabras de la lista
    palabra_minusc = palabra.lower()  # paso a minúsculas
    if palabra_minusc in sublista_previas:  # si la palabra actual está entre las anteriores... es solución buscada
        ### print("Palabra repetida:", palabra)
        ### Con mejora opcional: guardar los resultados (las repetidas) y así los mostramos sólo una vez
        if not palabra_minusc in soluciones:
            print("Palabra repetida:", palabra)  # la muestro original (no minúsc.) por claridad
            soluciones.append(palabra_minusc)
    
    sublista_previas.append(palabra_minusc)  # voy creando la lista de palabras previas (en minúsculas ya)
