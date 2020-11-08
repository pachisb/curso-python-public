#!/usr/bin/env python3
# -*- coding: utf-8 -*-


l = [1, 2, 3, 4, 5]
t = ('a', 'b', 'c', 'd')

# Función built-in zip(): "emparejar" dos iterables

z = zip(l, t)
# <zip at 0x1f032454100>

print(list(z))
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]


# Función built-in map()

def f(x):  # Función para aplicar a cada elemento
    y = 2 ** x
    return y

m = map(f, l)
# <map at 0x1f03240aac0>

print(list(m))
# [2, 4, 8, 16, 32]
