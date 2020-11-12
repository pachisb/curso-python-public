#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 7 (opcional) "billetes" del Módulo 5 (funciones)

# Solución con recursión (como se pedía)

def combinations(search):
    comb = []
    if search and len(search) > 0:
        if len(search) == 1:
            # caso trivial: para una lista de 1 elem., 2 posibles result.: elem. o nada
            return [search, []]
        else:
            # reducimos el problema a uno menor (el de n-1 elementos)
            current = search[0]
            new_search = search[1:]  # los n-1 del problema de menor tamaño
            temp_resul = combinations(new_search)
            # print('RECURSION new_search=', new_search, ' temp_result=', temp_resul)
            for r in temp_resul:
                # solución final A: el resultado de (n-1 elem.) tal cual
                comb.append(r)
                # solución final B: el resultado de (n-1 elem.) tal cual + el "actual"
                s = r + [ current ]
                comb.append(s)
    return comb


# Valores de entrada
change_for = 100
bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5]

result = combinations(bills)
print(len(result), "combinations found")

# Eliminar las duplicadas y/o que no cumplen el criterio (sumar "change_for")

# NOTA: podría hacerse muy abreviadamente con una "set comprehension" así
# final_result = { tuple(sorted(r, reverse=True)) for r in result if sum(r) == change_for }

final_result = set()  # para descartar repetidos!
for r in result:
    if sum(r) == change_for:
        # para el set necesitamos una tupla, por lo que la convertimos
        # y de paso la ordenamos (sólo por claridad al mostrarla), de mayor a menor
        final_result.add(tuple(sorted(r, reverse=True)))

print(len(final_result), "valid results:")
print(final_result)


# Resultado que tiene que salir para esos valores:
# {(20, 20, 20, 10, 10, 10, 10), (20, 20, 10, 10, 10, 10, 10, 5, 5), (20, 20, 20, 10, 10, 10, 5, 5)}
