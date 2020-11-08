#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Solución hecha en clase para el Ejercicio / demo "módulo my_rot13" del Módulo 6

# Ésta es la parte del módulo (este fichero es un módulo utilizable por otros)
# Se obtiene a su vez de lo hecho en clase para el Ejercicio / demo "ROT13" del Módulo 5

def print_rot13(frase):
    """Recibe una cadena como argumento para codificar ese mensaje, la
       convierte a mensaje encriptado e imprime en pantalla la nueva cadena
       encriptada"""

    DICCIONARIO = {
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
        "A": "N",
        "B": "O",
        "C": "P",
        "D": "Q",
        "E": "R",
        "F": "S",
        "G": "T",
        "H": "U",
        "I": "V",
        "J": "W",
        "K": "X",
        "L": "Y",
        "M": "Z",
    }

    frase_encriptada = ""
    for i in frase:
        if i in DICCIONARIO or i in DICCIONARIO.values():
            if i in DICCIONARIO.keys():
                frase_encriptada = frase_encriptada + DICCIONARIO[i]
            else:
                frase_encriptada = frase_encriptada + \
                    list(DICCIONARIO.keys())[
                        list(DICCIONARIO.values()).index(i)]
        else:
            frase_encriptada += i
    print(frase_encriptada)
