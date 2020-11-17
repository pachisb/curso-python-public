#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 2 "generadores y potencia" del Módulo 8

import time


# Caso de partida, con una función "normal" (no un generador)
def potencia(base, exponente):
    i = 1
    resul = 1
    while i <= exponente:
        resul = resul * base
        i = i + 1
    return resul


print(potencia(2, 20))


# Como generador, caso más sencillo (sin fin)
# def potencias_generador_sin_fin(base):
#     """Generador similar a potencia() pero que no termina nunca"""
#     i = 1
#     resul = 1
#     while True:
#         resul = resul * base
#         yield resul
#         i = i + 1
#     return resul


# Como generador, con mejora para que el fin sea opcional
def potencias_generador(base, inicio=1, fin=None):
    """Generador similar a potencia() pero que puede no terminar nunca"""
    i = inicio
    resul = base ** (inicio - 1)
    while fin is None or i <= fin:
        resul = resul * base
        yield resul
        i = i + 1
    return resul


# Uso indicando principio y fin
print("La lista con un generador es:")
print(list(potencias_generador(2, 1, 20)))


# Uso sin fin
print("La \"lista sin fin\" con un generador y comienzo en exp. 8 es:")
for i in potencias_generador(2, 8):
    print(i, end=" ")
    time.sleep(1)
