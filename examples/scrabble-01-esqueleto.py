#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 1 "Scrabble" del Módulo 10 (esqueleto inicial)
# NOTA: este fichero es el programa principal, que hace uso de otros dos módulos!

# Derived from: https://wiki.openhatch.org/wiki/O%27Reilly_Introduction_to_Python/Section_18

import sys
import scrabble_fich
import scrabble_reglas


def leer_argumentos_cli_letras():
    """Devuelve una LISTA con las letras recibidas como argumentos al programa, en MINÚSCULAS"""
    # ... COMPLETAR!
    return []


if __name__ == "__main__":

    WORD_LIST = "m10/sowpods.txt"
    print("Reading words file:", WORD_LIST)
    wordlist = scrabble_fich.leer_fichero_palabras(WORD_LIST)

    # Lista de letras con que contamos (recibidas como argumentos de línea de comandos desde el S.O.)
    rack = leer_argumentos_cli_letras()

    # Donde iremos guardando las soluciones encontradas
    valid_words = []

    # Forma FÁCIL de solucionarlo: recorrer cada palabra del "diccionario" (todas las válidas)
    # y comprobar si la podemos formar con las letras que tenemos.
    # Alt. mejor (avanzada): hacer combinaciones con nuestras letras, y buscarlas en el "dicc."
    for word in wordlist:
        # Make a copy of the rack for every new word, so we can manipulate it
        # without compromising the original rack.
        available_letters = rack[:]

        # ... COMPLETAR!
        word_is_valid = None  # MODIFICAR, se espera un booleano

        if word_is_valid:
            # Calculate the Scrabble score.
            score = scrabble_reglas.calcular_puntuacion_palabra(word)
            # Guardamos una TUPLA puntuación - palabra
            valid_words.append((score, word))

    for play in sorted(valid_words):
        print(play[0], play[1])
