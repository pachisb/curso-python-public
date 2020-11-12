#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio extra "saber si un número es primo" del Módulo 5 (funciones)

def has_divisor(n):
    """Dado un entero n >= 0, devuelve None si es primo, o el menor divisor encontrado si no"""
    factor = 2  # para iterar en los posibles divisores que iremos comprobando
    max_factor = int(round(n ** 0.5))  # máximo valor que puede tener un factor que sea divisor de n
    salto = 1

    while factor <= max_factor:
        if n % factor == 0:
            # print(f"Encontrado al menos un factor: {factor}")
            return factor  # no hace falta seguir
        # Opcional: mensaje informativo de vez en cuando si tardamos mucho...!
        if factor % 10_000_000 == 1:
            print(f"Diez millones de factores comprobados! ({factor // 1_000_000} total)")
        factor = factor + salto
        salto = 2  # después del 2, no hace falta comprobar ningún otro factor par!

    return None  # es primo


def is_prime(n):
    """Dado un entero n >= 0, devuelve True si es primo"""
    return has_divisor(n) is None


def divisor_list(n):
    """Dado un entero n >= 0, devuelve una lista con sus divisores enteros > 1"""
    l = []
    num = n
    divisor = has_divisor(num)
    while not divisor is None:
        # Había un factor divisor, guardarlo
        l.append(divisor)
        # Seguir calculando con el número dividido por él
        num = num // divisor
        divisor = has_divisor(num)
    
    l.append(num)
    return l


n = int(input("Número para comprobar? "))
esprimo = is_prime(n)
cad_solucion = esprimo and "sí" or "no"  # forma abreviada para no usar un if o similar...
print(f"El número {n} {cad_solucion} es primo")
print()

divisores = divisor_list(n)
print(f"El número {n} tiene los siguientes divisores > 1: {divisores}")
