#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 2 "funciones sencillas" del Módulo 5


import math


def area(r):
    return math.pi * r ** 2


print("Área del círculo:", area(5))


########################################################################


def maslarga(lista):
    lalarga = ""
    for palabra in lista:
        if len(palabra) > len(lalarga):
            lalarga = palabra
    return lalarga


lista = [
    "jaja",
    "holaquetalhola",
    "holaquetalytal",
    "palabra",
    "",
    "supercalifragilisticoespialidoso",
    "hola",
    "a",
]

print("Palabra más larga de la lista:", maslarga(lista))


########################################################################


def contarc(lista):
    car = 0
    for palabra in lista:
        car += len(palabra)
    return car


x = contarc(lista)
print("Hay", x, "caracteres en la lista")
