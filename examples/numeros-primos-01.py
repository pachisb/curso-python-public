#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio extra "saber si un número es primo" del Módulo 3 (con bucles)

# Posibles valores para hacer pruebas:
# Ejemplos de primos más o menos grandes: 191912783 y 122164747
# Ejemplo de no-primo muy grande: 23444976581260901 (producto de los dos anteriores)

n = int(input("Número para comprobar? "))


factor = 2  # para iterar en los posibles divisores que iremos comprobando
max_factor = int(round(n ** 0.5))  # máximo valor que puede tener un factor que sea divisor de n
es_primo = True  # supongo que lo es hasta no encontrar un factor que sea su divisor
salto = 1
while factor <= max_factor:
    if n % factor == 0:
        es_primo = False
        print(f"Encontrado al menos un factor: {factor}")
        break  # no hace falta seguir
    # Opcional: mensaje informativo de vez en cuando si tardamos mucho...!
    if factor % 1_000_000 == 1:
        print(f"Un millón de factores comprobados! ({factor // 1_000_000} total)")
    factor = factor + salto
    salto = 2  # después del 2, no hace falta comprobar ningún otro factor par!

cad_solucion = es_primo and "sí" or "no"  # forma abreviada para no usar un if o similar...
print(f"El número {n} {cad_solucion} es primo")
