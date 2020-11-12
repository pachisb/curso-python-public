#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# NOTA: esto "casi" equivale al módulo "this" (PEP 20: The Zen of Python)
# Se ha generado obteniendo su código fuente (en IPython: this??); también
# podría haberse hecho simplemente buscando el archivo "this.py" en la
# carpeta de instalación de Python... (subcarpeta "lib" - bibl. estándar)!

# Posteriormente, se han hecho mejoras (definir una función, y añadir la
# "parte __main__"... ver al final del todo). Con esos cambios, el uso
# esperado desde otro programa será:
#   import my_zen
#   my_zen.show_zen()  # en el caso de this no "hacía falta"; es mejor así!


# NOTA: esto es el contenido del texto/mensaje del Zen of Pyhton, pero
# encriptado con el algorimo ROT13 (...)
s = """Gur Mra bs Clguba, ol Gvz Crgref

Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""


def show_zen():
    """Función para desencriptar y escribir en pantalla el "Zen" de Python"""
    # Primero construir (de forma rebuscada) el diccionario con el que desencript.
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i+c)] = chr((i+13) % 26 + c)

    # De nuevo de forma poco clara, desencriptar (con una list comprehension que
    # a su vez hace uso del diccionario para ir "traduciendo" cada carácter...!)
    print("".join([d.get(c, c) for c in s]))


if __name__ == "__main__":
    # Si nos usan como programa independiente (no como módulo con import), ya
    # sea directamente (ejecutar desde VS Code o desde consola), o con py -m ...
    # se ejecutará esta parte. Es decir, se llamaa la función que "hace algo", y
    # en ese caso tendremos el mismo comportamiento que tenía el módulo "this"
    # pero siguiendo lo que se espera (no hacer lo mismo si nos usan con import!)
    show_zen()
