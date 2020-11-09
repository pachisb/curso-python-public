#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 7 (opcional) "billetes" del Módulo 5 (funciones)

# Solución con recursión (como se pedía)


def combinations(search, result=None):
    if result is None:
        # primera invocación, tomar un valor vacío para empezar
        result = []
    # Con esto (evitar generar/explorar duplicaciones) se vuelve "manejable"
    # Probar quitando el if, para ver la solución INEFICIENTE! (con > 10 billetes, lento)
    if not search in result:
        result.append(search)
        if len(search) > 1:
            for i in range(len(search)):
                new_search = search[:]  # copia
                del new_search[i]
                combinations(new_search, result)
    return result


# Valores de entrada
change_for = 100
bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5]

result = combinations(bills)
print(len(result), "combinations found")

# Eliminar las duplicadas y/o que no cumplen el criterio (sumar "change_for")
# y de paso ordenamos los billetes (sólo por claridad al mostrarlos), de mayor a menor
final_result = { tuple(sorted(r, reverse=True)) for r in result if sum(r) == change_for }
print(len(final_result), "valid results:")
print(final_result)


# Resultado que tiene que salir para esos valores:
# {(20, 20, 20, 10, 10, 10, 10), (20, 20, 10, 10, 10, 10, 10, 5, 5), (20, 20, 20, 10, 10, 10, 5, 5)}
