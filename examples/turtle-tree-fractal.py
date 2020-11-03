#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# From:
# https://towardsdatascience.com/creating-fractals-with-python-d2b663786da6

import turtle

MINIMUM_BRANCH_LENGTH = 5


def build_tree(t, branch_length, shorten_by, angle):
    if branch_length > MINIMUM_BRANCH_LENGTH:
        t.forward(branch_length)
        new_length = branch_length - shorten_by
        t.left(angle)
        build_tree(t, new_length, shorten_by, angle)
        t.right(angle * 2)
        build_tree(t, new_length, shorten_by, angle)
        t.left(angle)
        t.backward(branch_length)


t = turtle.Turtle()
# t.hideturtle()
t.setheading(90)
t.up()  # lápiz "arriba" (no pintar)
t.backward(100)
t.down()


t.color("green")
build_tree(t, 80, 10, 25)

# Pause at the end
turtle.mainloop()
