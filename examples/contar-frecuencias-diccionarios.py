#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio / demo "contar frecuencias" del Módulo 4

cadena = input("Escribe una lista de palabras separadas por espacios: ")
lista = cadena.split()
# print("LISTA:", lista)  # para depurar, opcional, quitar en la versión final
cuenta = {}


# Contar el número de apariciones de cada palabra
for palabra in lista:
    # Opcional: permitir mayúsculas y minúsculas indistintamente
    palabra = palabra.casefold()
    # Lee el valor actual (anterior), pero devuelve 0 si no existía
    valor_ant = cuenta.get(palabra, 0)
    cuenta[palabra] = valor_ant + 1
    ### Alternativa:
    ### if palabra in cuenta:
    ###     cuenta[valor_ant] = cuenta[valor_ant] + 1
    ### else:
    ###     cuenta[valor_ant] = 0

# Mostrar los resultados que cumplen lo que se nos pide
for palabra_dicc, frecuencia in cuenta.items():
    if frecuencia > 2:
        # print("La palabra", palabra_dicc, "aparece", frecuencia, "veces")
        print(f"La palabra '{palabra_dicc}' aparece {frecuencia} veces")
