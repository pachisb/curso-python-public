#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio / demo "media con listas" del Módulo 4

cadena = input("Dame la lista de números separados por espacios: ")

lista = []
suma = 0.0
for palabra in cadena.split():
    f = float(palabra)
    lista.append(f)

# print(lista)
suma = sum(lista)
media = suma / len(lista)
print(f"La suma es {suma} y la media es {media}.")


# Opcional: mediana. Necesitamos ordenar la lista (y para ello, imprescind. que sea de números)

lista = cadena.split()
for i in range(len(lista)):
    lista[i] = float(lista[i])
lista.sort()
# print(lista)
suma = sum(lista)

if len(lista) % 2 == 1:
    # Lista con número impar de elementos: el del medio es la mediana
    pos = len(lista) // 2  # como las posiciones empiezan en 0, así me sirve
    mediana = lista[pos]
else:
    pos = len(lista) // 2
    mediana = (lista[pos - 1] + lista[pos]) / 2

print(f"La mediana es {mediana}.")
