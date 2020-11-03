#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ejemplos para entender el orden de las sentencias con la recursión


############################################################################

# Primer ejemplo: factorial

def factorial(n):
    if n <= 1:
        # Caso trivial o base
        return 1 
    else:
        return n * factorial(n - 1) 

print("El factorial de 5 es:", factorial(5))
print()


############################################################################


# Ejemplo de función que va haciendo operaciones varias

def baja_y_sube(primero, n):
    if n > 0:
        print("PRE: ", primero, n)
        primero += 1
        n -= 1
        baja_y_sube(primero, n)
        print("POST: ", primero, n)
    else:
        print("TERMINADO!")


baja_y_sube(1, 5)
print()

baja_y_sube(7, 3)
print()


############################################################################


# Otro ejemplo más "útil": imprimir en orden inverso una lista de valores

def al_reves(l):
    if len(l) > 1:
        sublista = l[1:]
        # "soluciono" (con recursión) el problema de los n-1 elementos SIGUIENTES
        al_reves(sublista)
        # y después escribo el primer (actual) elemento, con lo que lo hago al final
        # y con ello soluciono el problema completo (n elementos)
        print(l[0])
    else:
        # Caso trivial: lista de 1 elemento, al revés es ella misma
        print(l[0])


al_reves([1, 2, 5, 7, 8, 99])
