#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Soluciones hechas en clase para el Ejercicio / demo "ROT13" del Módulo 5

abc = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9,
       "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18,
       "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25, }

num_abc = {"0": "a", "1": "b", "2": "c", "3": "d", "4": "e", "5": "f", "6": "g", "7": "h",
           "8": "i", "9": "j", "10": "k", "11": "l", "12": "m", "13": "n", "14": "o",
           "15": "p", "16": "q", "17": "r", "18": "s", "19": "t", "20": "u", "21": "v",
           "22": "w", "23": "x", "24": "y", "25": "z", }


def print_rot13(frase):
    traduc = ""
    for letra in frase.casefold():  # Mejorado: convertir a minúsculas (mejor que nada)
        if letra in abc:
            pos1 = abc[letra]
            if pos1 < 13:
                pos2 = pos1+13
            else:
                pos2 = pos1-13
            pos3 = str(pos2)  # Mejora posible: no hacer esto, y que num_abc tenga claves numéricas
            result = num_abc[pos3]
        else:
            result = letra
        traduc = traduc+result
    print(traduc)


frase = (input("Introduce una frase para encriptar: "))
print()
print("La frase encriptada queda:")
print_rot13(frase)
print()


######################################################################################


diccionario = {
    "a": "n",
    "b": "o",
    "c": "p",
    "d": "q",
    "e": "r",
    "f": "s",
    "g": "t",
    "h": "u",
    "i": "v",
    "j": "w",
    "k": "x",
    "l": "y",
    "m": "z",
}


def print_rot13(frase):
    """Recibe una cadena como argumento para codificar ese mensaje, la
       convierte a mensaje encriptado e imprime en pantalla la nueva cadena
       encriptada
    """
    frase_encriptada = ""

    for i in frase.casefold():
        if i in diccionario or i in diccionario.values():
            if i in diccionario.keys():
                frase_encriptada = frase_encriptada + diccionario[i]
            else:
                frase_encriptada = frase_encriptada + \
                    list(diccionario.keys())[
                        list(diccionario.values()).index(i)]
        else:
            frase_encriptada += i
    print(frase_encriptada)


frase = input("Mensaje a encriptar: ")
print()
print("La frase encriptada queda:")
print_rot13(frase)
print()


######################################################################################


import codecs


def print_rot13(x):
    """Introduce una cadena para encriptar o desencriptar."""
    frase_encriptada = codecs.encode(x, "rot13")
    print(frase_encriptada)


frase = input("Mensaje a encriptar: ")
print()
print("La frase encriptada queda:")
print_rot13(frase)
print()
