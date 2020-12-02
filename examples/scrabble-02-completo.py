#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 1 "Scrabble" del Módulo 10 (COMPLETA)
# NOTA: este fichero es el programa principal, que hace uso de otros dos módulos!

# Derived from: https://wiki.openhatch.org/wiki/O%27Reilly_Introduction_to_Python/Section_18

import sys
import scrabble_fich
import scrabble_reglas


def leer_argumentos_cli_letras():
    """Devuelve una LISTA con las letras recibidas como argumentos al programa, en MINÚSCULAS"""
    if len(sys.argv) < 2:
        print("Usage: scrabble.py [RACK_OF_LETTERS]")
        # sys.exit(1)
        # DEBUG ONLY: Use some (fixed) test data instead of error+stop
        return list("akxktywio")
    else:
        return list(sys.argv[1].lower())


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

        word_is_valid = True
        for letter in word:
            if letter not in available_letters:
                word_is_valid = False
                break
            # Eliminamos la letra "usada" de la lista de disponibles
            available_letters.remove(letter)

        if word_is_valid:
            # Calculate the Scrabble score.
            score = scrabble_reglas.calcular_puntuacion_palabra(word)
            valid_words.append((score, word))  # guardamos una TUPLA puntuación - palabra

    for play in sorted(valid_words):
        print(play[0], play[1])
