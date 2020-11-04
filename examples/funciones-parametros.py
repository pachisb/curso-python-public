#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 4 "parámetros" del Módulo 5


def irpf(base, irpf=12.5, pagas_extras=False):
    """
    Devuelve el importe de la parte del IRPF correspondiente a la base recibida.
    NOTA: la base (y el tipo o % de IRPF opcional) has de ser float, o devolverá None.
    """
    if pagas_extras == True:
        prorrateo = base / 6
        base = base + prorrateo

    if type(base) == float and type(irpf) == float:
        return round(base * irpf / 100.0, 2)  # Mejora opcional: redondeado a 2 decimales
    else:
        return None


print(irpf(1100.0))
print(irpf(base=1000.0))
print(irpf(irpf=10.5, base=1234.5, pagas_extras=True))
