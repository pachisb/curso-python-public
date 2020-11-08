#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución hecha en clase para el Ejercicio / demo "módulo my_rot13" del Módulo 6

# Ésta es la parte del programa de test (este programa hace uso del módulo my_rot13)
# Se obtiene a su vez de lo hecho en clase para el Ejercicio / demo "ROT13" del Módulo 5

import my_rot13

fraset = input("Mensaje a encriptar: ")
print()
print("La frase encriptada queda:")
my_rot13.print_ro13(frase)
print()
