#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 5 "copo de nieve Koch" del Módulo 5 (esqueleto inicial)

import turtle


def koch(t, order, size):
    """
    Make turtle t draw a Koch fractal of 'order' and 'size'.
    Leave the turtle facing the same direction.
    """
    # MODIFICAR ESTA PARTE !!!
    t.forward(size)


t = turtle.Turtle()

# Dibujar el fractal de Koch varias veces (con distinto 'orden')
for i in (0, 1, 2, 3, 4):
    # Las tres líneas siguientes, simplemente para ubicar cada uno OK
    t.up()  # Pencil up
    t.goto(-150, 300 - i * 150)
    t.down()

    # Dibujar el fractal de orden i
    koch(t, i, 300)

# Pause at the end
turtle.mainloop()
