#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio / demo "recorrer diccionarios" del Módulo 4 (COMPLETA)

dicc1 = {
    "Naranjas": 25,
    "Manzanas": True,
    "Fresas": 240,
    "Kiwis": 15.33333,
    "Plátanos": 5.5,
}

dicc2 = {
    "Naranjas": None,
    "Manzanas": "55",
    "ZZZ": (0, 998, 'Canarias'),
    "YYY": 'algunos',
    "Fresas": "0.0",
    "Peras": True,
    "Kiwis": "3",
    "Plátanos": 5.5,
}

frutas = dicc2


# Primera forma de solucionarlo: recorriendo las claves del diccionario

# for fruta in frutas:  # si no indico nada, es igual que frutas.keys()
#     # Comprobar si el tipo del dato cumple lo que nos pedían...
#     if (type(frutas[fruta]) == int) or (type(frutas[fruta]) == float):
#         print("La cantidad de:", fruta, "es", frutas[fruta])

# print()


# Alternativa: recorrer los elementos o items (tuplas clave-valor)

for fruta, cantidad in frutas.items():
    # Comprobar si el tipo del dato cumple lo que nos pedían...
    if (type(cantidad) == int) or (type(cantidad) == float):
        print("La cantidad de:", fruta, "es", frutas[fruta])
    # NOTA: opcionalmente permitimos también cadenas con "pinta" de números
    elif type(cantidad) == str:
        try:  # pero con esto controlamos (e ignoramos) posibles errores!
            x = float(cantidad)
            print("La cantidad de:", fruta, "es", x)
        except:
            pass

print()


# Alternativa 2, no recomendable para este caso: sacar los elementos con popitem()
# No es recomendable simplemente por eficiencia, tenemos que hacer primero una copia
# porque no sabemos si luego haría falta la lista original de nuevo (probable...)

# copia_frutas = frutas.copy()  # hacer una copia
# while len(copia_frutas) > 0:
#     fruta, cantidad = copia_frutas.popitem()  # saca uno y nos devuelve clave-valor
#     # Y todo lo demás, igual que en el caso anterior (...)
#     ...
