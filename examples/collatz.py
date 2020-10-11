#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input("Número para empezar? "))

# Escribir la secuencia Collatz o "3n+1" hasta 1
while n != 1:
    print(n, end=", ")
    if n % 2 == 0:  # par
        n = n // 2
    else:
        n = n * 3 + 1
print(n, end=".\n")
