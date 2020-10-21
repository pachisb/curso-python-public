#!/usr/bin/env python3
# -*- coding: utf-8 -*-

floatstr = input("Dame un número flotante para a: ")
a = float(floatstr)
floatstr = input("Dame un número flotante para b: ")
b = float(floatstr)
floatstr = input("Dame un número flotante para c: ")
c = float(floatstr)

# Calcular el discriminante, que es lo que no debe ser
# negativo si queremos soluciones reales (no imaginarias)
discrim = b * b - (4 * a * c)

if discrim < 0:
    print("Error, no hay solución con números reales")
else:
    x1 = ((-b) + discrim ** 0.5) / (2 * a)
    x2 = ((-b) - discrim ** 0.5) / (2 * a)
    if x1 == x2:  # caso especial: dos soluciones iguales (x1 == x2)
        print("La solución unica (doble) es:", x1)
    else:
        print("Solución 1:", x1)
        print("Solución 2:", x2)
