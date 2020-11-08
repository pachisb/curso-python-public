#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio extra "generadores y números primos" del Módulo 8 (esqueleto inicial)


# Alternativa: hacerlo usando el módulo ya creado!
# import my_primos


def has_divisor(n):
    """Dado un entero n >= 0, devuelve None si es primo, o el menor divisor encontrado si no"""
    factor = 2  # para iterar en los posibles divisores que iremos comprobando
    max_factor = int(round(n ** 0.5))
    salto = 1

    while factor <= max_factor:
        if n % factor == 0:
            return factor  # no hace falta seguir
        factor = factor + salto
        salto = 2  # después del 2, no hace falta comprobar ningún otro factor par!

    return None  # es primo


def is_prime(n):
    """Dado un entero n >= 0, devuelve True si es primo"""
    return has_divisor(n) is None


# infinite prime generator
def infinite_primes(inicio=2):
    """Generador "infinito" de números primos"""
    # MODIFICAR / COMPLETAR !!!
    pass


for i in infinite_primes():
    print(i, end=" ")

    # optional: stop after some time
    digits = len(str(i))
    if digits == 4:
        break
