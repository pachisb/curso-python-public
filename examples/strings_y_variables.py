#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = "Hola"
saludo = f"{s}, mundo"
print(saludo)
print(f"{saludo}!")
print()

unic = "\N{WINKING FACE}"
unic2 = "😉"
print(unic)
print(unic == unic2)
print(ord(unic))
print(unic.encode("utf-8"))
print()

年 = 2018
print(年)
عام = 2019
print(عام)
print(type(عام))
print()

hola = 5.0
print(f"{{hola, {hola=}")
print(f"{{hola, {hola!s}")
print(f"{{hola, {5 * 5:x}")
