#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 3 "polígonos y tortugas" del Módulo 3

# Variable para el número de lados del polígono
n = 0

# Pido el número de lados deseado, y opcionalmente repito hasta que el valor sea aceptable (> 2)
while n <= 2:
    n = int(input("Dime el número de lados (entero, > 2): "))


### NOTA: he movido aquí la parte del inicio (tal cual, sin modificar) para que la ventana
### de dibujo aparezca después de haber pedido el valor de n al usuario (así no "molesta"...)
import turtle
# Inicialización: crear una "tortuga" t. Dejar tal cual
t = turtle.Turtle()
# t.hideturtle()  # opcional: no mostrar la tortuga (menos didáctico)
# Posición inicial no centrada (opcional, se puede modif./eliminar)
t.up()  # lápiz "arriba" (no pintar)
t.goto(-50, 250)  # movimiento directo a coordenadas, por sencillez (no es lo habitual)
t.down()


# Cálculo del ángulo, variable según el número de lados
angle = 360 / n
SIDE_LENGTH = 300
# Mejora opcional: usar una longitud de lado de polígonos variable (útil para valores de n grandes)
side_length = 300
# Cálculo totalmente inventado: para que se "ajuste" en función de n...
while side_length * n > 1200:
    side_length /= 1.5

contador = 0
while contador < n:
    t.forward(side_length)  # side_length o SIDE_LENGTH según queramos longitud de lados variable o fija
    t.right(angle)
    contador += 1  # contador = contador + 1


### NOTA: el bucle anterior (el principal), pero hecho usando for, y TOTALMENTE EQUIVALENTE, sería:
### for i in range(n):  # i realmente no la uso, pero tomará valores desde 0 hasta n-1; contador ni la necesito!
###    t.forward(side_length)  # side_length o SIDE_LENGTH según queramos longitud de lados variable o fija
###    t.right(angle)


# Esto es necesario para que la ventana no se cierre al final. Dejar tal cual
turtle.mainloop()
