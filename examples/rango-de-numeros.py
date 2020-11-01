#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 1 "rango de números" del Módulo 4 (con bucles y listas)

# Valores para los "parámetros" de entrada
inicio = 0
fin = 12
salto = 3  # para la mejora opcional que nos piden: permitir saltos > 1


lista_num = []  # comenzamos con una lista vacía
i = inicio
while i < fin:
    lista_num.append(i)
    i = i + salto  # sin la parte opcional, sería sumando siempre 1

print("La lista final es:", lista_num)


# Esto, como comprobación solamente...
lista_num = []  # comenzamos con una lista vacía
for i in range(inicio, fin, salto):
    lista_num.append(i)
    # lista_num = lista_num + [i]  # alternativa a append()

# NOTA: más sencillo aún, todo el bucle anterior equivale a:
# lista_num = list(range(inicio, fin, salto))

print("La lista generada a través de range() es:", lista_num)
