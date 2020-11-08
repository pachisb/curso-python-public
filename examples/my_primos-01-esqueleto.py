#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio extra "saber si un número es primo" del Módulo 6 (módulos) (esqueleto inicial)
# NOTA: Renombrar (y opc. mover) este fichero para que cumpla las reglas de nombres de módulos!

def has_divisor(n):
    """Dado un entero n >= 0, devuelve None si es primo, o el menor divisor encontrado si no"""

    # COMPLETAR...!!!

    return None  # es primo


def is_prime(n):
    """Dado un entero n >= 0, devuelve True si es primo"""
    return has_divisor(n) is None


def divisor_list(n):
    l = []

    # COMPLETAR...!!!

    return l


# También podemos definir constantes y/o variables en el módulo
# IMPORTANTE: esta parte, como todas (incluida la de __main__) se ejecuta UNA SOLA VEZ

# En este caso, definimos por comodidad unos valores que sirven para hacer pruebas:
# Ejemplos de primos más o menos grandes: 122164747 y 191912783
# Ejemplo de no-primo muy grande: 23444976581260901 (producto de los dos anteriores)

SAMPLE_PRIME = 122164747
SAMPLE_PRIME_2 = 191912783
SAMPLE_NON_PRIME = 23444976581260901
