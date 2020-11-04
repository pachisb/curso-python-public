#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 1 "borrar de una lista" del Módulo 5
# Para entender el concepto de parámetros por asignacion (hacer copia de ellos cuando conviene)


def print_all_after_delete_first(a):
    """Modifica la lista recibida! OK si es lo que queremos, pero si no... ver función siguiente"""
    del a[0]
    print(a)


def print_all_except_first(l):
    """No modifica la lista recibida"""
    a = l.copy()
    del a[0]
    print(a)


# Alternativa/mejora: con una sola función, podemos tener ambos comportamientos
# Para ello, es imprescindible en este caso otro parámetro, para que el usuario elija el deseado
def print_all_after_delete_first_or_not(l, operate_on_copy=False):
    """Modifica o no la lista recibida"""
    if operate_on_copy:
        a = l.copy()
    else:
        a = l

    del a[0]
    print(a)


lista = [1, 2, 3, 4, 5, 6]
print_all_after_delete_first(lista)
print(lista)  # el primer elemento ya no estará
print_all_after_delete_first(lista)
print(lista)  # ahora el segundo tampoco
print()


print_all_except_first(lista)
print(lista)  # no ha cambiado la lista en este caso
print()


lista = [1, 2, 3, 4, 5, 6]
print_all_after_delete_first_or_not(lista, operate_on_copy=True)
print(lista)  # no ha cambiado la lista tampoco
print()
