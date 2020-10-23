#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución 2 para el Ejercicio 4 "buscar repetidos" del Módulo 3

cadena = input("Escribe una lista de palabras separadas por espacios: ")
palabra = ""
soluciones = ""
subcadena = ""

# Por si acaso no terminaba con un espacio, se lo añadimos para que la última palabra funcione OK
cadena += " "

for letra in cadena:
    # print("LETRA:", letra)  # para depurar, opcional, quitar en la versión final
    if letra != " " and letra !="," and letra != "." and letra != "\n" and letra != "\t": 
        palabra += letra  # aún sigue la palabra actual: la vamos guardando "a mano", carácter a carácter
        # print("PALABRA:", palabra)  # para depurar, opcional
    else:
        # print("PALABRA TERMINADA:", palabra)  # para depurar, opcional
        # print("SUBCADENA:", subcadena)  # para depurar, opcional
        if not subcadena.find(palabra) == -1:
            ### ORIGINAL: hemos encontrado una repetida (lo que piden), así que la mostramos y listo
            ### print("SOLUCION:", palabra)
            ### MEJORADO: guardamos los resultados (las repetidas) y así los mostramos sólo una vez
            if soluciones.find(palabra) == -1:
                print("SOLUCION SIN REPETICIONES:", palabra)
                soluciones += palabra + " "
                # print("SOLUCIONES:", soluciones)  # para depurar, opcional
        subcadena += palabra
        palabra = ""

# NOTA: en el original (pueden aparecer varias veces los repetidos), al haber procesado las
# palabras a mano buscando los espacios, pueden pasar "cosas raras" si hay varios seguidos...

# NOTA 2: esta versión mejorada del algoritmo no tiene el problema de las "subpalabras", por qué?
