#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución 4 para el Ejercicio / demo "ROT13" del Módulo 5


def print_rot13(frase):
    traduc = ""

    for caracter in frase:
        if caracter >= 'a' and caracter <= 'z':
            pos1 = ord(caracter) - ord('a')
            pos2 = ( pos1 + 13 ) % 26
            caracter = chr( ord('a') + pos2 )
        elif caracter >= 'A' and caracter <= 'Z':
            pos1 = ord(caracter) - ord('A')
            pos2 = ( pos1 + 13 ) % 26
            caracter = chr( ord('A') + pos2 )
        traduc = traduc + caracter
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
