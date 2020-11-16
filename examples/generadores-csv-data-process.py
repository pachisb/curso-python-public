#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# From: https://realpython.com/introduction-to-python-generators/#using-generators
# © 2012–2020 Real Python

# forma preferible (es un generador)
def csv_reader(file_name):
    # va leyendo del fichero (tipo texto, UTF-8) línea a línea,
    # y devolviéndolas una cada vez
    for row in open(file_name, "r", encoding="utf-8"):
        yield row

# equivalent generator expression (generator comprehension)
# csv_gen = (row for row in open(file_name))


# equivalente ineficiente (lee todo el fichero primero -> falla si muy grande)
def csv_reader_slow(file_name):
    file = open(file_name, "r", encoding="utf-8")
    # lee todo de una vez (lento, y consume mucha más memoria!) y lo convierte en una
    # lista mediante split(), para devolverla "entera"
    rows = file.read().split("\n")
    # NOTA: si el fichero termina con \n (habitual) en realidad teníamos 1 fila de más!
    if rows[-1] == "":
        del rows[-1]
    return rows


# NOTA: probar cambiando el nombre del fichero para usar uno muy grande!
csv_gen = csv_reader("prac/weather.csv")
row_count = 0
for row in csv_gen:
    row_count += 1
print(f"Row count is {row_count}")
print(f"Last row was {row}")

# NOTA: probar cambiando el nombre del fichero para usar uno muy grande!
# csv_gen = csv_reader_slow("prac/python_psf_external_19.csv")
# csv_gen = csv_reader_slow("prac/weather.csv")
csv_gen = csv_reader_slow("examples/flashcards_capitales.csv")
row_count = 0
for row in csv_gen:
    row_count += 1
print(f"Row count slow is {row_count}")
print(f"Last row was {row}")
