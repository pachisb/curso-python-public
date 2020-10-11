#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import turtle

# Inicialización: crear una "tortuga" t. Dejar tal cual
t = turtle.Turtle()
# t.hideturtle()  # opcional: no mostrar la tortuga (menos didáctico)

# Posición inicial no centrada (opcional, se puede modif./eliminar)
t.up()  # lápiz "arriba" (no pintar)
t.goto(-150, 150)  # movimiento directo a coordenadas, por sencillez (no es lo habitual)
t.down()

# El dibujo en sí.
# === INICIO PARTE A MODIFICAR ===
SIDE_LENGTH = 300
angle = 90

t.forward(SIDE_LENGTH)
t.right(angle)
t.forward(SIDE_LENGTH)
t.right(angle)
t.forward(SIDE_LENGTH)
t.right(angle)
t.forward(SIDE_LENGTH)
t.right(angle)
# === FIN DE PARTE A MODIFICAR ===

# Esto es necesario para que la ventana no se cierre al final. Dejar tal cual
turtle.mainloop()
