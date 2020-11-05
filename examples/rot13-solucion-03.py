#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución 3 para el Ejercicio / demo "ROT13" del Módulo 5


def print_rot13(frase):
    LETRAS_ABC = "abcdefghijklmnopqrstuvwxyz"
    LETRAS_MAY_ABC = LETRAS_ABC.upper()
    traduc = ""

    for letra in frase:
        if letra in LETRAS_ABC:
            pos1 = LETRAS_ABC.index(letra)
            pos2 = ( pos1 + 13 ) % 26
            letra = LETRAS_ABC[pos2]
        elif letra in LETRAS_MAY_ABC:
            pos1 = LETRAS_MAY_ABC.index(letra)
            pos2 = ( pos1 + 13 ) % 26
            letra = LETRAS_MAY_ABC[pos2]
        traduc = traduc + letra
    print(traduc)


# Por comodidad, encripto ya de entrada dos mensajes para probar el funcionamiento
print_rot13("This is a sample string 'converted' with rot13")
print_rot13("¡Esto es otro ejemplo de una cadena en español, con eñes y puntuación!")


frase = input("Introduce una frase para encriptar: ")
# Por comodidad, permito seguir encriptando mientras se introduzca algo de texto
while frase:
    print()
    print("La frase encriptada queda:")
    print_rot13(frase)
    print()
    frase = input("Introduce una frase para encriptar: ")
