#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 5 "copo de nieve Koch" del Módulo 5 (COMPLETA, FINAL)

# Based on the samples from:
# https://openbookproject.net/thinkcs/python/english3e/recursion.html#drawing-fractals

import turtle


def koch(t, order, size):
    """
    Make turtle t draw a Koch fractal of 'order' and 'size'.
    Leave the turtle facing the same direction.
    """
    if order == 0:  # The base case is just a straight line
        t.forward(size)
    else:
        koch(t, order - 1, size / 3)  # Go 1/3 of the way
        t.left(60)
        koch(t, order - 1, size / 3)
        t.right(120)
        koch(t, order - 1, size / 3)
        t.left(60)
        koch(t, order - 1, size / 3)


t = turtle.Turtle()
t.up()  # Pencil up
t.goto(-150, 100)
t.down()

# Dibujar el fractal de Koch varias veces
ORDEN = 3  # Probar con 2 y 4 para menos o más detalle (y lentitud)
LADOS = 3
LONGITUD_LADO = 300

for i in range(LADOS):
    koch(t, ORDEN, LONGITUD_LADO)
    t.right(360 / LADOS)

# Pause at the end
turtle.mainloop()
