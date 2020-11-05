#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Soluciones hechas en clase para el Ejercicio 6 "potencia de un número" del Módulo 5 (con recursión)


# Solución 1: Fila penultima

def potencia(base, exponente):
    if exponente < 0:
        # Mejora interesante: aceptar (y gestionar bien) exponentes negativos
        return 1 / potencia(base, -exponente)
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente-1)


x = potencia(2, -2)
print(x)


############################################################################


# Solución 2: Fila del fondo

# Con print()'s útiles para entender el orden de ejecución!

def potencia(base, exponente):
    if exponente < 0:
        # Devuelvo un error intencionadamente, mejor que no parar "nunca"
        return None
    elif exponente == 0:
        print("Caso base: termino y devuelvo:", exponente)
        return 1
    else:
        print("El valor a calcular es 2 **", exponente)
        print("    para eso, antes calcularé: potencia( base, ", exponente - 1, ")")
        valor = potencia(base, exponente - 1)
        print("    el resultado recibido ha sido:", valor)
        valor = base * valor
        print("    mi resultado final es:", valor)
        return valor


x = potencia(2, 6)
print(x)
