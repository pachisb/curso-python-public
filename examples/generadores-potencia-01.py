#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Soluciones hechas en clase para el Ejercicio 2 "generadores y potencia" del Módulo 8


# Solución segunda fila

def potencia(base, exponente):
    for i in range(exponente):
        yield base ** exponente

# Forma de uso/consumo compacta, pero que sirve sólo si TIENE fin!
l = list(potencia(5, 8))
print(l)

#################################################

# Solución última fila

def potencia(base, exponente):
    i = 0
    result = 1
    while i < exponente:
        result = base*result
        i += 1
        yield result
    return

# Forma de uso/consumo sencilla
for i in potencia(5, 3):
    print(i)

#################################################

# Solución primera fila

def potencia(base):
    """Genera las potencias del número recibido, empezando en 1 (sin fin)"""
    exponente=1
    while True:
        yield base**exponente
        exponente+=1

# Forma de uso/consumo en la que el final se controla desde
# aquí (consumidor), o sea, da igual si el generador no tiene fin
for i in potencia(2):
    if i > 1_000_000:
        break
    print(i)

# Similar pero con un while, es mucho más complejo
# porque el for ya hace todo esto "por nosotros"...!
# i = 0
# it = potencia(2)
# while i < 100:
#     print(it.__next__())
#     i += 1
