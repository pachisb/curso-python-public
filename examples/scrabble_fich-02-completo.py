#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 1 "Scrabble" del Módulo 10 (COMPLETA)
# NOTA: Renombrar este fichero para que tenga el nombre de módulo que se espera!

# Derived from: https://wiki.openhatch.org/wiki/O%27Reilly_Introduction_to_Python/Section_18

def leer_fichero_palabras(filename):
    """Devuelve una LISTA de cadenas con las palabras que contiene el fichero indicado.
    Todas están en MINÚSCULAS"""
    wordlist = []
    try:
        with open(filename) as wordlist:
            for word in wordlist:
                # Get rid of newlines, spaces, etc with strip()
                wordlist = [word.lower().strip() for word in wordlist]
    except:
        print("Error leyendo fichero:", filename)
        wordlist = []  # por si acaso, no devolver nada

    return wordlist
