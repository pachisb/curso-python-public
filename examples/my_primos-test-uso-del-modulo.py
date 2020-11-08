#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio extra "saber si un número es primo" del Módulo 6 (módulos)

# Ésta es la parte del programa de test (este programa hace uso del módulo my_primos)

import my_primos

n = my_primos.SAMPLE_PRIME

esprimo = my_primos.is_prime(n)
cad_solucion = esprimo and "sí" or "no"  # forma abreviada para no usar un if o similar...
print(f"El número {n} {cad_solucion} es primo")

divisores = my_primos.divisor_list(n)
print(f"El número {n} tiene los siguientes divisores > 1: {divisores}")
