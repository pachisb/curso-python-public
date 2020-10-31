#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 6 "modificar diccionarios" del Módulo 6
# (ampliación del Ejercicio / demo "recorrer diccionarios" del Módulo 4, añadiendo proveedor)
# Solución de la cuarta fila de clase

# Ventajas de esta estr. para los datos: es más expresiva y más fácilmente ampliable, y
# seguramente sirva mejor para otros tipos de cálculos y operaciones
# Desventajas: tal como está ahora mismo, no permite varios proveedores para un producto!
frutas = {
    "Naranjas 🍊": {"cantidad": 25, "proveedor": "p1"},
    "Manzanas 🍏": {"cantidad": 1, "proveedor": "p2"},
    "Fresas 🍓": {"cantidad": 240, "proveedor": "p3"},
    "Kiwis 🥝": {"cantidad": 15.33333, "proveedor": "p1"},
    "Plátanos 🍌": {"cantidad": 5.5, "proveedor": "p2"},
}


# Usamos un diccionario auxiliar sencillo clave-valor (proveedor-peso total), ej.: { "p1" : 25 }
pesos_subtotal = {}

# Recorrer todos los productos e ir acumulando según/donde corresponda sus pesos...
for fruta in frutas.keys():
    print("La cantidad de", fruta, "es", frutas[fruta]["cantidad"])
    prov = frutas[fruta]["proveedor"]
    # Ojo, en el diccionario auxiliar la primera vez no habrá nada, tengo que gestionarlo
    if prov in pesos_subtotal:
        pesos_subtotal[prov] = pesos_subtotal[prov] + frutas[fruta]["cantidad"]
    else:
        pesos_subtotal[prov] = frutas[fruta]["cantidad"]
    # Alternativa mejor: con get(), que lee el valor, pero devuelve 0 si no existe
    # pesos_subtotal[prov] = pesos_subtotal.get(prov, 0) + frutas[fruta]["cantidad"]

# Escribir la solución
print()

for prov in pesos_subtotal.keys():
    print("La cantidad del proveedor", prov, "es", pesos_subtotal[prov])
