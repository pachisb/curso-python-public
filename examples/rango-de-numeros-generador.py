#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio / demo "generadores y range" del Módulo 8

import time


# Caso de partida, con una función normal
def my_range(inicio, fin, salto=1):
    """Función similar a range() pero que devuelve una lista"""
    res = []
    i = inicio
    while i < fin:
        res.append(i)
        i = i + salto
    return res


lista_num = my_range(3, 24, 4)
print("La lista final es:", lista_num)

# Esto, como comprobación solamente...
# lista_num = list(range(3, 24, 4))
# print("La lista generada a través de range() es:", lista_num)


# Como generador (fin y salto opcionales)
def my_range_generator(inicio, fin=None, salto=1):
    """Generador similar a range() pero que puede no terminar nunca"""
    # NOTA: en realidad se parece más aún a count() del módulo itertools
    # https://docs.python.org/3.9/library/itertools.html?highlight=range%20count#itertools.count
    res = []  # comenzamos con una lista vacía
    i = inicio
    while fin is None or i < fin:
        yield i
        i = i + salto
    return res


lista_num = my_range_generator(3, 24, 4)
print("La lista final con un generador es:", list(lista_num))

# Uso sin fin
print("La \"lista sin fin\" con un generador es:")
for i in my_range_generator(3, None, 4):
    print(i, end=" ")
    time.sleep(1)
