#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 6 "modificar diccionarios" del Módulo 6
# (ampliación del Ejercicio / demo "recorrer diccionarios" del Módulo 4, añadiendo proveedor)
# Solución de la primera fila de clase

# Ventajas de esta estr. para los datos: es más sencilla, y sirve bien para lo que justo se pide
# Desventajas: no es fácilmente ampliable para más datos (ej. origen) ni describe lo contenido
frutas = {
    "Prov.A": {"Naranjas 🍊": 25, "Fresas 🍓": 240},
    "Prov.B": {"Manzanas 🍏": 0, "Naranjas 🍊": 12.5, "Plátanos 🍌": 80},
    "Prov.C": {"Kiwis 🥝": 15, "Plátanos 🍌": 5},
}


# Calcular y escribir las soluciones directamente
# En este caso es sencillo (bucles anidados) porque la estr. de los datos lo "facilita" (...)
suma = 0
for proveedor in frutas.keys():
    suma = 0
    for k, v in frutas[proveedor].items():
        print("La cantidad de", k, "es", v)
        suma = suma + v
    print(proveedor, suma)
