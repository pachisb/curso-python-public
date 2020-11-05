#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución 2 para el Ejercicio / demo "ROT13" del Módulo 5


def print_rot13(frase):
    LETRAS_ABC = "abcdefghijklmnopqrstuvwxyz"
    DICC_ABC = { "a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25 }
    traduc = ""

    for caracter in frase:
        # Simplificación: tratar mayúsc. y minúsc. igual. Cómo se debería hacer si no?
        letra = caracter.casefold()
        # El bloque siguiente "traduce" la letra si era del conjunto a..z solamente
        if letra in LETRAS_ABC:
            pos1 = DICC_ABC[letra]
            if pos1 < 13:
                pos2 = pos1 + 13
            else:
                pos2 = pos1 - 13
            letra = LETRAS_ABC[pos2]
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
